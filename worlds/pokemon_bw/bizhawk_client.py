import math
from typing import TYPE_CHECKING, Any, Coroutine

import orjson

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from CommonClient import logger
from .client.locations import check_flag_locations, check_dex_locations
from .client.items import receive_items
from .client.goals import get_method
from .client.setup import early_setup, late_setup

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


def register_client():
    """This is just a placeholder function to remind new (and old) world devs to import the client file"""
    pass


class PokemonBWClient(BizHawkClient):
    game = "Pokemon Black and White"
    system = "NDS"
    patch_suffix = (".apblack", ".apwhite")

    ram_read_write_domain = "Main RAM"
    rom_read_only_domain = "ROM"
    flags_amount = 2912
    flag_bytes_amount = math.ceil(flags_amount/8)
    dex_amount = 650
    dex_bytes_amount = math.ceil(dex_amount/8)
    main_items_bag_size = 1240//4  # 310
    key_items_bag_size = 332//4  # 83
    tm_hm_bag_size = 436//4  # 109
    medicine_bag_size = 192//4  # 48
    berry_bag_size = 256//4  # 64

    data_address_address = 0x000024  # says 0x21B310 in vanilla W
    ingame_state_address = 0x000034
    var_offset = 0x209BC  # 0x23BCCC in vanilla W
    flags_offset = 0x20C38  # 0x23BF48 in vanilla W
    dex_offset = 0x21EC4  # 0x23D1D4 in vanilla W
    main_items_bag_offset = 0x18cbc  # 0x233FCC in vanilla W
    key_items_bag_offset = 0x19194  # 0x2344A4 in vanilla W
    tm_hm_bag_offset = 0x192e0  # 0x2345F0 in vanilla W
    medicine_bag_offset = 0x19494  # 0x2347A4 in vanilla W
    berry_bag_offset = 0x19554  # 0x234864 in vanilla W
    badges_offset = 0x21ac0  # 0x23CDD0 in vanilla W

    def __init__(self):
        super().__init__()
        self.slot_data: dict[str, Any] = {}
        self.flags_cache: bytearray = bytearray(self.flag_bytes_amount)
        self.dex_cache: bytearray = bytearray(self.dex_bytes_amount)
        self.player_name: str = ""
        self.missing_flag_locations: list[list[str]] = [[]]*self.flags_amount
        self.missing_dex_flag_locations: list[list[str]] = [[]]*self.dex_amount
        self.location_name_to_id: dict[str, int] | None = None
        self.location_id_to_name: dict[int, str] | None = None
        self.item_id_to_name: dict[int, str] | None = None
        self.save_data_address = 0
        self.received_items_count = 0
        self.goal_checking_method: Coroutine[Any, Any, bool] | None = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        """Should return whether the currently loaded ROM should be handled by this client. You might read the game name
        from the ROM header, for example. This function will only be asked to validate ROMs from the system set by the
        client class, so you do not need to check the system yourself.

        Once this function has determined that the ROM should be handled by this client, it should also modify `ctx`
        as necessary (such as setting `ctx.game = self.game`, modifying `ctx.items_handling`, etc...)."""
        from .rom import cached_rom
        from ndspy.rom import NintendoDSRom

        rom = cached_rom[0]
        if rom is None:
            file = await bizhawk.read(ctx.bizhawk_ctx, (
                (0, 268435456, self.rom_read_only_domain),
            ))
            rom = NintendoDSRom(file[0])
        header: tuple[bytes, bytes] = (rom.name, rom.idCode)
        if header not in ((b'POKEMON B', b'IRBO'), (b'POKEMON W', b'IRAO')):
            # raise Exception("Rom appears to not be an english copy of Pokémon Black or White Version.")
            return False
        try:
            self.slot_data = orjson.loads(rom.getFileByName("patch/slot_data.json"))
        except ValueError:
            # raise Exception("Rom appears to be an unpatched copy. "
            #                 "Use the provided patch file to obtained a patched rom.")
            return False
        self.player_name = self.slot_data["player_name"]
        self.location_name_to_id: dict[str, int] = self.slot_data["data_package"]["location_name_to_id"]
        self.location_id_to_name = {loc_id: name for name, loc_id in self.location_name_to_id.items()}
        self.item_id_to_name = self.slot_data["data_package"]["item_id_to_name"]
        self.goal_checking_method = get_method(self, ctx)
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = False
        ctx.watcher_timeout = 1
        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        """Should set ctx.auth in anticipation of sending a `Connected` packet. You may override this if you store slot
        name in your patched ROM. If ctx.auth is not set after calling, the player will be prompted to enter their
        username."""

        ctx.auth = self.player_name

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        """For handling packages from the server. Called from `BizHawkClientContext.on_package`."""
        from .data.locations import all_item_locations, dexsanity

        if cmd == 'Connected':
            for loc_id in ctx.missing_locations:
                loc_name = self.location_id_to_name[loc_id]
                if loc_name in all_item_locations:
                    self.missing_flag_locations[all_item_locations[loc_name].flag_id].append(loc_name)
                elif loc_name in dexsanity.location_table:
                    self.missing_dex_flag_locations[dexsanity.location_table[loc_name].dex_number].append(loc_name)
                else:
                    logger.warn(f"Missing location \"{loc_name}\" neither flag nor dex location")
        elif cmd == "RoomInfo":
            ctx.seed_name = args["seed_name"]

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        """Runs on a loop with the approximate interval `ctx.watcher_timeout`. The currently loaded ROM is guaranteed
        to have passed your validator when this function is called, and the emulator is very likely to be connected."""

        try:
            if not ctx.server or not ctx.server.socket.open or ctx.server.socket.closed:
                return
            read = await bizhawk.read(
                ctx.bizhawk_ctx, (
                    (self.ingame_state_address, 1, self.ram_read_write_domain),
                )
            )
            if read[0][0] == 0:
                return
            setup_needed = False
            if self.save_data_address == 0:
                await early_setup(self, ctx)
                setup_needed = True

            locations_to_check: list[int] = (
                await check_flag_locations(self, ctx) +
                await check_dex_locations(self, ctx)
            )
            if len(locations_to_check) != 0:
                await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locations_to_check)}])

            await receive_items(self, ctx)

            if await self.goal_checking_method:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

            if setup_needed:
                await late_setup(self, ctx)

        except bizhawk.RequestFailedError:
            pass

        except bizhawk.ConnectorError:
            pass

