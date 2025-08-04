from typing import TYPE_CHECKING

from ...locations import PokemonBWLocation

if TYPE_CHECKING:
    from ... import PokemonBWWorld
    from BaseClasses import Region
    from ...data import RulesDict


def lookup(area: int) -> dict[str, int]:
    from ...data.locations.ingame_items.other import table

    return {
        name: data.flag_id * 100 + area + (
            int(name[:-2].split("#")[-1]) if "#" in name else 0
        )
        for name, data in table.items()
    }


def create(world: PokemonBWWorld, regions: dict[str, Region], rules: RulesDict) -> None:
    from ...data.locations.ingame_items.other import table

    for name, data in table.items():
        r: Region = regions[data.region]
        l: PokemonBWLocation = PokemonBWLocation(world.player, name, world.location_name_to_id[name], r)
        l.progress_type = data.progress_type(world)
        if data.rule is not None:
            l.access_rule = rules[data.rule]
        r.locations.append(l)
