from BaseClasses import CollectionState
from .. import ExtendedRule
from ..pokemon import pokedex, species


# Standard requirements

def has_species(name: str) -> ExtendedRule:
    return lambda state, world: state.has(name, world.player)


def has_number_of_species(x: int) -> ExtendedRule:
    # As wild encounters aren't the only way to see different species, we are going to assume that we will always be
    # able to see 115 species (practical maximum for x) by the time we reach the league
    return lambda state, world: (
        state.count_from_list_unique(pokedex.by_name, world.player) >= x
        or state.can_reach_region("Pokémon League", world.player)
    )


def has_item(name: str, amount: int = 1) -> ExtendedRule:
    return lambda state, world: state.has(name, world.player, amount)


def has_any_item(*items: str) -> ExtendedRule:
    return lambda state, world: state.has_any(items, world.player)


def can_reach_region(region: str) -> ExtendedRule:
    return lambda state, world: (state.can_reach_region(region, world.player))


# HM requirements

can_use_strength: ExtendedRule = lambda state, world: (
    state.has("HM04", world.player)
    and state.has_any(world.strength_species, world.player)
)

can_use_surf: ExtendedRule = lambda state, world: (
    state.has("HM03", world.player)
    and state.has_any(world.surf_species, world.player)
)

can_use_cut: ExtendedRule = lambda state, world: (
    state.has("HM01", world.player)
    and state.has_any(world.cut_species, world.player)
)

can_use_waterfall: ExtendedRule = lambda state, world: (
    state.has_all(("HM03", "HM05"), world.player)
    and state.has_any(world.surf_species, world.player)
    and state.has_any(world.waterfall_species, world.player)
)

can_use_dive: ExtendedRule = lambda state, world: (
    state.has_all(("HM03", "HM06"), world.player)
    and state.has_any(world.surf_species, world.player)
    and state.has_any(world.dive_species, world.player)
)


# Miscellaneous requirements

has_fighting_type_species: ExtendedRule = lambda state, world: (
    state.has_any(world.fighting_type_species, world.player)
)
