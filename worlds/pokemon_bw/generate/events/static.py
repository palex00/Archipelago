from typing import TYPE_CHECKING, Callable

from ...locations import PokemonBWLocation
from BaseClasses import ItemClassification, CollectionState
from ...items import PokemonBWItem

if TYPE_CHECKING:
    from ... import PokemonBWWorld
    from BaseClasses import Region
    from ...data import SpeciesData, RulesDict


def create(world: "PokemonBWWorld", regions: dict[str, "Region"], rules: "RulesDict") -> set[tuple[str, int]]:
    from ...data.locations.encounters.static import static, legendary, gift, trade
    from ...data.pokemon.species import by_id as species_by_id, by_name as species_by_name
    from ...data.pokemon.movesets import table as movesets_table
    from ...data import TradeEncounterData, StaticEncounterData

    catchable_dex_form: set[tuple[str, int]] = set()

    def get_trade_rule(x: str) -> Callable[[CollectionState], bool]:
        return lambda state: state.has(x, world.player)

    def f(table: dict[str, StaticEncounterData | TradeEncounterData]):
        for name, data in table.items():
            if type(data) is TradeEncounterData or ((data.inclusion_rule is None) or data.inclusion_rule(world)):
                r: "Region" = regions[data.encounter_region]
                l: PokemonBWLocation = PokemonBWLocation(world.player, name, None, r)
                species_id: tuple[int, int] = data.species_black \
                    if world.options.version == "black" else data.species_white
                species_name: str = species_by_id[species_id]
                item: PokemonBWItem = PokemonBWItem(species_name, ItemClassification.progression, None, world.player)
                l.place_locked_item(item)
                if type(data) is StaticEncounterData:
                    if data.access_rule is not None:
                        l.access_rule = rules[data.access_rule]
                elif world.options.version == "black":
                    l.access_rule = get_trade_rule(species_by_id[(data.wanted_black, 0)])
                else:
                    l.access_rule = get_trade_rule(species_by_id[(data.wanted_white, 0)])
                r.locations.append(l)

                species_data: "SpeciesData" = species_by_name[species_name]
                catchable_dex_form.add((species_data.dex_name, species_id[1]))
                moveset: set[str] = movesets_table[species_name].tm_hm_moves
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
                if "Fighting" in (species_data.type_1, species_data.type_2):
                    world.fighting_type_species.add(species_name)

    f(static)
    f(legendary)
    f(gift)
    f(trade)

    return catchable_dex_form
