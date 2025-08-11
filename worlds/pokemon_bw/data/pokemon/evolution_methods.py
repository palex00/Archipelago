from .. import EvolutionMethodData, ExtendedRule
from . import species


def has_species(name: str) -> ExtendedRule:
    return lambda state, world: state.has(name, world.player)


always_possible: ExtendedRule = lambda state, world: True
can_reach_magnetic_area: ExtendedRule = lambda state, world: state.can_reach_region("Chargestone Cave", world.player)
can_reach_moss_rock: ExtendedRule = lambda state, world: state.can_reach_region("Pinwheel Forest West", world.player)
can_reach_ice_rock: ExtendedRule = lambda state, world: state.can_reach_region("Twist Mountain", world.player)

can_buy_item: dict[int, ExtendedRule] = {
    80: lambda state, world: state.can_reach_region("Twist Mountain", world.player),  # Sun Stone
    81: lambda state, world: state.can_reach_region("Twist Mountain", world.player),  # Moon Stone
    82: lambda state, world: state.can_reach_region("Castelia City", world.player),  # Fire Stone
    83: lambda state, world: state.can_reach_region("Chargestone Cave", world.player),  # Thunderstone
    84: lambda state, world: state.can_reach_region("Castelia City", world.player),  # Water Stone
    85: lambda state, world: state.can_reach_region("Castelia City", world.player),  # Leaf Stone
    107: lambda state, world: state.can_reach_region("Route 10", world.player),  # Shiny Stone
    108: lambda state, world: state.can_reach_region("Route 10", world.player),  # Dusk Stone
    109: lambda state, world: state.can_reach_region("Route 10", world.player),  # Dawn Stone
    110: lambda state, world: state.can_reach_region("Route 9", world.player),  # Oval Stone
    221: lambda state, world: state.can_reach_region("Route 9", world.player),  # King's Rock
    226: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Deep Sea Tooth
    227: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Deep Sea Scale
    233: lambda state, world: state.can_reach_region("Chargestone Cave", world.player),  # Metal Coat
    235: lambda state, world: state.can_reach_region("Route 9", world.player),  # Dragon Scale
    252: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Up-Grade
    321: lambda state, world: state.can_reach_region("Route 9", world.player),  # Protector
    322: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Electirizer
    323: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Magmarizer
    324: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Dubious Disc
    325: lambda state, world: state.can_reach_region("Route 9", world.player),  # Reaper Cloth
    326: lambda state, world: state.can_reach_region("Giant Chasm Entrance Cave", world.player),  # Razor Claw
    327: lambda state, world: state.can_reach_region("Giant Chasm Entrance Cave", world.player),  # Razor Fang
    537: lambda state, world: state.can_reach_region("Undella Town", world.player),  # Prism Scale
}

methods: dict[str, EvolutionMethodData] = {
    "Level up": EvolutionMethodData(0, lambda value: always_possible),
    "Stone": EvolutionMethodData(0, lambda value: can_buy_item[value]),
    "Stone male": EvolutionMethodData(0, lambda value: can_buy_item[value]),  # Repeatable encounters, including static, are ensured
    "Stone female": EvolutionMethodData(0, lambda value: can_buy_item[value]),  # Repeatable encounters, including static, are ensured
    "Friendship": EvolutionMethodData(0, lambda value: always_possible),
    "Friendship (Day)": EvolutionMethodData(0, None),  # Removed
    "Friendship (Night)": EvolutionMethodData(0, None),  # Removed
    "Trade": EvolutionMethodData(0, None),  # Removed
    "Trade with item": EvolutionMethodData(0, None),  # Removed
    "Trade Karrablast Shelmet": EvolutionMethodData(0, None),  # Removed
    "Magnetic area": EvolutionMethodData(0, lambda value: can_reach_magnetic_area),
    "Level up with move": EvolutionMethodData(0, lambda value: always_possible),  # When randomized evolutions, then move id must be taken from level up moveset
    "Level up moss rock": EvolutionMethodData(0, lambda value: can_reach_moss_rock),
    "Level up ice rock": EvolutionMethodData(0, lambda value: can_reach_ice_rock),
    "Level up item day": EvolutionMethodData(0, lambda value: can_buy_item[value]),  # Always paired with night
    "Level up item night": EvolutionMethodData(0, lambda value: can_buy_item[value]),  # Always paired with day
    "Level up higher defense": EvolutionMethodData(0, lambda value: always_possible),
    "Level up higher attack": EvolutionMethodData(0, lambda value: always_possible),
    "Level up equal physical": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Silcoon": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Cascoon": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Ninjask": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Shedinja": EvolutionMethodData(0, lambda value: always_possible),
    "Level up high beauty": EvolutionMethodData(0, None),  # Removed
    "Level up (female)": EvolutionMethodData(0, lambda value: always_possible),  # Repeatable encounters, including static, are ensured
    "Level up (male)": EvolutionMethodData(0, lambda value: always_possible),  # Repeatable encounters, including static, are ensured
    "Level up with party member": EvolutionMethodData(0, lambda value: has_species(species.by_id[value, 0])),
}
