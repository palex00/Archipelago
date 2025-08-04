from typing import TYPE_CHECKING

from BaseClasses import Location, Region

if TYPE_CHECKING:
    from . import PokemonBWWorld
    from .data import RulesDict


class PokemonBWLocation(Location):
    game = "Pokemon Black and White"


def get_location_lookup_table() -> dict[str, int]:
    from .generate.locations import overworld_items, hidden_items, other, badge_rewards, tm_hm, dexsanity

    return {
        **overworld_items.lookup(100000),
        **hidden_items.lookup(200000),
        **other.lookup(300000),
        **badge_rewards.lookup(400000),
        **tm_hm.lookup(500000),
        **dexsanity.lookup(600000),
    }


def get_regions(world: PokemonBWWorld) -> dict[str, Region]:
    from .data.locations import regions
    from .data.locations.encounters import regions as encounter_regions

    return {
        name: Region(name, world.player, world.multiworld)
        for name in regions.region_list
    } | {
        name: Region(name, world.player, world.multiworld)
        for name in encounter_regions.region_list
    }


def create_rule_dict(world: PokemonBWWorld) -> RulesDict:
    from .data.locations.rules import extended_rules_list

    return {rule: (lambda state: rule(state, world)) for rule in extended_rules_list}


def create_and_place_event_locations(world: PokemonBWWorld, regions: dict[str, Region],
                                     rules: RulesDict) -> set[tuple[str, int]]:
    """Returns a set of species that are actually catchable in this world."""
    from .generate.events import wild, static, evolutions

    catchable_dex_form: set[tuple[str, int]] = wild.create(world, regions) | static.create(world, regions, rules)
    evolutions.create(world, regions, catchable_dex_form)
    return catchable_dex_form


def create_and_place_locations(world: PokemonBWWorld, regions: dict[str, Region],
                               rules: RulesDict, catchable_dex_form: set[tuple[str, int]]) -> None:
    from .generate.locations import overworld_items, hidden_items, other, badge_rewards, tm_hm, dexsanity

    overworld_items.create(world, regions, rules)
    hidden_items.create(world, regions, rules)
    other.create(world, regions, rules)
    badge_rewards.create(world, regions, rules)
    tm_hm.create(world, regions, rules)
    dexsanity.create(world, regions, catchable_dex_form)


def connect_regions(world: PokemonBWWorld, regions: dict[str, Region], rules: RulesDict) -> None:
    pass


def cleanup_regions(regions: dict[str, Region]) -> None:
    pass


def place_locked_items(world: PokemonBWWorld, regions: dict[str, Region]) -> None:
    pass


def count_to_be_filled_locations(regions: dict[str, Region]) -> int:
    pass
