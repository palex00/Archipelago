
from typing import TYPE_CHECKING, Coroutine, Any, Callable
import worlds._bizhawk as bizhawk

if TYPE_CHECKING:
    from ..bizhawk_client import PokemonBWClient
    from worlds._bizhawk.context import BizHawkClientContext


def get_method(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> Callable[
    ["PokemonBWClient", "BizHawkClientContext"], Coroutine[Any, Any, bool]
]:

    match client.slot_data["goal"]:
        case "ghetsis":
            return defeat_ghetsis
        case "champion":
            return become_champion
        case "cynthia":
            return defeat_cynthia
        # case "regional_pokedex":
        # case "national_pokedex":
        # case "custom_pokedex":
        case "tmhm_hunt":
            return verify_tms_hms
        case "seven_sages_hunt":
            return find_seven_sages
        case _:
            client.logger.warning("Bad goal in slot data: "+client.slot_data["goal"])
            return error


async def defeat_ghetsis(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    return client.flags_cache[2400//8] & 1 != 0


async def become_champion(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    return client.flags_cache[2427//8] & 8 != 0


async def defeat_cynthia(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    read = await bizhawk.read(
        ctx.bizhawk_ctx, (
            (client.save_data_address + client.var_offset + (2 * 0xE4), 1, client.ram_read_write_domain),
        )
    )
    return read[0][0] >= 2


async def verify_tms_hms(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    return client.flags_cache[0x191//8] & 2 != 0


async def find_seven_sages(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    read = await bizhawk.read(
        ctx.bizhawk_ctx, (
            (client.save_data_address + client.var_offset + (2 * 0xCC), 1, client.ram_read_write_domain),
        )
    )
    return read[0][0] >= 6 and client.flags_cache[2400//8] & 1 != 0


async def error(client: "PokemonBWClient", ctx: "BizHawkClientContext") -> bool:
    return False
