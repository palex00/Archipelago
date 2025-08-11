from typing import TYPE_CHECKING, Callable

from ...locations import PokemonBWLocation
from BaseClasses import ItemClassification, CollectionState
from ...items import PokemonBWItem

if TYPE_CHECKING:
    from ... import PokemonBWWorld
    from BaseClasses import Region
    from ...data import SpeciesData, EvolutionMethodData, ExtendedRule, RulesDict


def create(world: "PokemonBWWorld", regions: dict[str, "Region"], catchable_dex_form: set[tuple[str, int]]) -> None:
    from ...data.pokemon.species import by_id as species_by_id, by_name as species_by_name
    from ...data.pokemon.pokedex import by_name as pokedex_by_name
    from ...data.pokemon.movesets import table as movesets_table
    from ...data.pokemon.evolution_methods import methods, extended_rules_list

    def f(r: "ExtendedRule") -> Callable[[CollectionState], bool]:
        return lambda state: r(state, world)

    region: "Region" = regions["Evolutions"]
    rules: "RulesDict" = {ext_rule: f(ext_rule) for ext_rule in extended_rules_list}
    new_catchable: set[tuple[str, int]] = catchable_dex_form.copy()
    next_catchable: set[tuple[str, int]] = set()

    def get_rule(current_evolution: tuple[str, int, str]) -> Callable[[CollectionState], bool]:
        method: "EvolutionMethodData" = methods[current_evolution[0]]
        ext_rule: "ExtendedRule" = method.rule(current_evolution[1])
        if ext_rule in rules:
            return rules[ext_rule]
        else:
            return lambda state: ext_rule(state, world)

    while len(new_catchable) > 0:
        for dex_form in new_catchable:
            dex_num: int = pokedex_by_name[dex_form[0]]
            species_name: str = species_by_id[(dex_num, dex_form[1])]
            data: "SpeciesData" = species_by_name[species_name]

            for x in range(len(data.evolutions)):
                evolution: tuple[str, int, str] = data.evolutions[x]
                name = f"Evolving {species_name} {x+1}"
                location: PokemonBWLocation = PokemonBWLocation(world.player, name, None, region)
                item: PokemonBWItem = PokemonBWItem(evolution[2], ItemClassification.progression, None, world.player)
                location.place_locked_item(item)
                location.access_rule = get_rule(evolution)
                region.locations.append(location)

                evo_data: "SpeciesData" = species_by_name[evolution[2]]
                evo_dex_form: tuple[str, int] = (evo_data.dex_name, evo_data.form)
                catchable_dex_form.add(evo_dex_form)
                if evo_dex_form not in new_catchable:
                    next_catchable.add(evo_dex_form)
                moveset: set[str] = movesets_table[evolution[2]].tm_hm_moves
                if "HM04" in moveset:
                    world.strength_species.add(evolution[2])
                if "HM01" in moveset:
                    world.cut_species.add(evolution[2])
                if "HM03" in moveset:
                    world.surf_species.add(evolution[2])
                if "HM06" in moveset:
                    world.dive_species.add(evolution[2])
                if "HM05" in moveset:
                    world.waterfall_species.add(evolution[2])
                if "Fighting" in (evo_data.type_1, evo_data.type_2):
                    world.fighting_type_species.add(evolution[2])

        new_catchable = next_catchable
        next_catchable = set()




