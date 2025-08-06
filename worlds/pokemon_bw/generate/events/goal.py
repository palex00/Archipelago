from typing import TYPE_CHECKING, Callable

from ...locations import PokemonBWLocation
from BaseClasses import ItemClassification, CollectionState
from ...items import PokemonBWItem

if TYPE_CHECKING:
    from ... import PokemonBWWorld
    from BaseClasses import Region
    from ...data import SpeciesData


def create(world: PokemonBWWorld, regions: dict[str, Region]) -> None:

    item: PokemonBWItem = PokemonBWItem("Goal", ItemClassification.progression, None, world.player)
    location: PokemonBWLocation
    rule: Callable[[CollectionState], bool]
    match world.options.goal.current_key:
        case "ghetsis":
            location = PokemonBWLocation(world.player, "Defeat Ghetsis", None, regions["N's Castle"])
            regions["N's Castle"].locations.append(location)
        case "champion":
            location = PokemonBWLocation(world.player, "Defeat Alder", None, regions["Pokémon League"])
            regions["Pokémon League"].locations.append(location)
        case "cynthia":
            location = PokemonBWLocation(world.player, "Defeat Cynthia", None, regions["Undella Town"])
            regions["Undella Town"].locations.append(location)
        # case "regional_pokedex":
        # case "national_pokedex":
        # case "custom_pokedex":
        case "tmhm_hunt":
            from ...data.items.tm_hm import table
            location = PokemonBWLocation(world.player, "Verify TMs/HMs", None, regions["Castelia City"])
            regions["Castelia City"].locations.append(location)
            location.access_rule = lambda state: state.has_all(table, world.player)
        case "seven_sages_hunt":
            location = PokemonBWLocation(world.player, "Find all seven sages", None, regions["N's Castle"])
            regions["N's Castle"].locations.append(location)
            location.access_rule = lambda state: (
                # Finding Ghetsis is checked by setting N's Castle as the region
                state.can_reach_location("Route 18 - TM from sage Rood", world.player) and
                state.can_reach_location("Dreamyard - TM from sage Gorm", world.player) and
                state.can_reach_location("Relic Castle - TM from sage Ryoku", world.player) and
                state.can_reach_location("Cold Storage - TM from sage Zinzolin", world.player) and
                state.can_reach_location("Chargestone Cave - TM from sage Bronius", world.player) and
                state.can_reach_location("Route 14 - TM from sage Giallo", world.player)
            )
        case _:
            raise Exception(f"Bad goal option: {world.options.goal.current_key}")
    location.place_locked_item(item)
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Goal", world.player)
