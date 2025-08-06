import time
from typing import TYPE_CHECKING

from NetUtils import ClientStatus
import asyncio

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


def register_client():
    """This is just a placeholder function to remind new (and old) world devs to import the client file"""
    pass


class PokemonBWClient(BizHawkClient):
    game = "Sonic Rush"
    system = "NDS"
    patch_suffix = (".apblack", ".apwhite")

    ram_read_write_domain = "Main RAM"
    rom_read_only_domain = "ROM"

    def __init__(self):
        super().__init__()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        """Should return whether the currently loaded ROM should be handled by this client. You might read the game name
        from the ROM header, for example. This function will only be asked to validate ROMs from the system set by the
        client class, so you do not need to check the system yourself.

        Once this function has determined that the ROM should be handled by this client, it should also modify `ctx`
        as necessary (such as setting `ctx.game = self.game`, modifying `ctx.items_handling`, etc...)."""
        rom = await bizhawk.read(ctx.bizhawk_ctx, (
            (0, 268435456, self.rom_read_only_domain),
        ))
        pass

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        """Should set ctx.auth in anticipation of sending a `Connected` packet. You may override this if you store slot
        name in your patched ROM. If ctx.auth is not set after calling, the player will be prompted to enter their
        username."""
        pass

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        """For handling packages from the server. Called from `BizHawkClientContext.on_package`."""
        pass

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        """Runs on a loop with the approximate interval `ctx.watcher_timeout`. The currently loaded ROM is guaranteed
        to have passed your validator when this function is called, and the emulator is very likely to be connected."""
        pass
