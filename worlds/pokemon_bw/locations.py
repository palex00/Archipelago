from typing import TYPE_CHECKING, Callable

from BaseClasses import Location, Region, CollectionState

if TYPE_CHECKING:
    from . import PokemonBWWorld
    from .data import RulesDict, ExtendedRule, AccessRule
    from .data import SpeciesData


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


def get_regions(world: "PokemonBWWorld") -> dict[str, Region]:
    from .data.locations import regions
    from .data.locations.encounters import regions as encounter_regions

    return {
        name: Region(name, world.player, world.multiworld)
        for name in regions.region_list
    } | {
        name: Region(name, world.player, world.multiworld)
        for name in encounter_regions.region_list
    }


def create_rule_dict(world: "PokemonBWWorld") -> "RulesDict":
    from .data.locations.rules import extended_rules_list

    def f(r: "ExtendedRule") -> Callable[[CollectionState], bool]:
        return lambda state: r(state, world)

    return {rule: f(rule) for rule in extended_rules_list} | {None: None}


def create_and_place_event_locations(world: "PokemonBWWorld") -> dict[str, "SpeciesData"]:
    """Returns a dict of species that are actually catchable in this world."""
    from .generate.events import wild, static, evolutions, goal, species_tables

    catchable_species_data: dict[str, "SpeciesData"] = wild.create(world) | static.create(world)
    evolutions.create(world, catchable_species_data)
    species_tables.populate(world, catchable_species_data)
    goal.create(world)
    return catchable_species_data


def create_and_place_locations(world: "PokemonBWWorld", catchable_species_data: dict[str, "SpeciesData"]) -> None:
    from .generate.locations import overworld_items, hidden_items, other, badge_rewards, tm_hm, dexsanity

    overworld_items.create(world)
    hidden_items.create(world)
    other.create(world)
    badge_rewards.create(world)
    tm_hm.create(world)
    dexsanity.create(world, catchable_species_data)


def connect_regions(world: "PokemonBWWorld") -> None:
    from .data.locations import region_connections as gameplay_connections
    from .data.locations.encounters import region_connections as encounter_connections

    # Create gameplay region connections
    for name, data in gameplay_connections.connections.items():
        world.regions[data.exiting_region].connect(
            world.regions[data.entering_region], name, world.rules_dict[data.rule]
        )

    def combine_and(connection_rules: tuple["ExtendedRule", ...]) -> "AccessRule":
        def f(state) -> bool:
            for r in connection_rules:
                if not r(state, world):
                    return False
            return True
        return f

    for name, data in encounter_connections.connections.items():
        if (data.inclusion_rule is None) or data.inclusion_rule(world):
            if data.rules not in world.rules_dict:
                # Assuming single rules are already in rules because of extended_rules_list
                world.rules_dict[data.rules] = combine_and(data.rules)
            world.regions[data.exiting_region].connect(
                world.regions[data.entering_region], name, world.rules_dict[data.rules]
            )

    world.multiworld.register_indirect_condition(
        world.regions["Mistralton Cave Inner"], world.get_entrance("Pinwheel Forest east")
    )
    world.multiworld.register_indirect_condition(
        world.regions["N's Castle"], world.get_entrance("Relic Castle B5F castleside")
    )


def cleanup_regions(regions: dict[str, Region]) -> None:
    to_remove = []
    for name, region in regions.items():
        if len(region.entrances) == 0 and region.name != "Menu":
            to_remove.append(name)
    for name in to_remove:
        regions.pop(name)


def count_to_be_filled_locations(regions: dict[str, Region]) -> int:
    count = 0
    for region in regions.values():
        for location in region.locations:
            if location.item is None:
                count += 1
    return count
