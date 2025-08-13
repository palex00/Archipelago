from typing import TYPE_CHECKING

from ...locations import PokemonBWLocation
from BaseClasses import ItemClassification
from ...items import PokemonBWItem

if TYPE_CHECKING:
    from ... import PokemonBWWorld
    from BaseClasses import Region
    from ...data import SpeciesData


def create(world: "PokemonBWWorld", regions: dict[str, "Region"]) -> set[tuple[str, int]]:
    from ...data.locations.encounters.slots import table
    from ...data.pokemon.species import by_id as species_by_id, by_name as species_by_name

    catchable_dex_form: set[tuple[str, int]] = set()
    is_black = world.options.version == "black"

    for name, data in table.items():
        if data.encounter_region in regions:
            r: "Region" = regions[data.encounter_region]
            l: PokemonBWLocation = PokemonBWLocation(world.player, name, None, r)
            species_id: tuple[int, int] = data.species_black if is_black else data.species_white
            species_name: str = species_by_id[species_id]
            item: PokemonBWItem = PokemonBWItem(species_name, ItemClassification.progression, None, world.player)
            l.place_locked_item(item)
            r.locations.append(l)

            species_data: "SpeciesData" = species_by_name[species_name]
            catchable_dex_form.add((species_data.dex_name, species_id[1]))

    return catchable_dex_form
