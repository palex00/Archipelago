from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ... import PokemonBWWorld


def populate(world: "PokemonBWWorld", catchable_name_form: set[tuple[str, int]]) -> None:
    from ...data.pokemon import pokedex, species, movesets

    for name_form in catchable_name_form:
        species_name = species.by_id[(pokedex.by_name[name_form[0]], name_form[1])]
        species_data = species.by_name[species_name]
        moveset = movesets.table[species_name].tm_hm_moves
        if "HM04" in moveset:
            world.strength_species.add(species_name)
        if "HM01" in moveset:
            world.cut_species.add(species_name)
        if "HM03" in moveset:
            world.surf_species.add(species_name)
        if "HM06" in moveset:
            world.dive_species.add(species_name)
        if "HM05" in moveset:
            world.waterfall_species.add(species_name)
        if "TM70" in moveset:
            world.flash_species.add(species_name)
        if "Fighting" in (species_data.type_1, species_data.type_2):
            world.fighting_type_species.add(species_name)
