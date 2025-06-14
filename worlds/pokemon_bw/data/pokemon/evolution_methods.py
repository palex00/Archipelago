from typing import Callable

from BaseClasses import CollectionState
from . import EvolutionMethodData, species, ExtendedRule


always_possible: ExtendedRule = lambda state, world: True


def can_reach_region(region: str) -> ExtendedRule:
    return lambda state, world: state.can_reach_region(region, world.player)


def has_species(name: str) -> ExtendedRule:
    return lambda state, world: state.has(name, world.player)


# TODO fix ids
methods: dict[str, EvolutionMethodData] = {
    "Level up": EvolutionMethodData(0, lambda value: always_possible),
    "Stone": EvolutionMethodData(0, None),  # TODO Need to find some way to not loose access once achieved
    "Stone male": EvolutionMethodData(0, None),  # TODO Need to find some way to not loose access once achieved
    "Stone female": EvolutionMethodData(0, None),  # TODO Need to find some way to not loose access once achieved
    "Friendship": EvolutionMethodData(0, lambda value: always_possible),
    "Friendship (Day)": EvolutionMethodData(0, lambda value: always_possible),
    "Friendship (Night)": EvolutionMethodData(0, lambda value: always_possible),
    "Trade": EvolutionMethodData(0, None),  # TODO Need to get rid of trade evolutions
    "Trade with item": EvolutionMethodData(0, None),  # TODO Need to get rid of trade evolutions
    "Trade Karrablast Shelmet": EvolutionMethodData(0, None),  # TODO Need to get rid of trade evolutions
    "Magnetic area": EvolutionMethodData(0, lambda value: can_reach_region("Chargestone Cave")),
    "Level up with move": EvolutionMethodData(0, lambda value: always_possible),
    "Level up moss rock": EvolutionMethodData(0, lambda value: can_reach_region("Pinwheel Forest West")),
    "Level up ice rock": EvolutionMethodData(0, lambda value: can_reach_region("Twist Mountain")),
    "Level up item day": EvolutionMethodData(0, None),  # TODO Need to find some way to not loose access once achieved
    "Level up item night": EvolutionMethodData(0, None),  # TODO Need to find some way to not loose access once achieved
    "Level up higher defense": EvolutionMethodData(0, lambda value: always_possible),
    "Level up higher attack": EvolutionMethodData(0, lambda value: always_possible),
    "Level up equal physical": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Silcoon": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Cascoon": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Ninjask": EvolutionMethodData(0, lambda value: always_possible),
    "Level up Shedinja": EvolutionMethodData(0, lambda value: always_possible),
    "Level up high beauty": EvolutionMethodData(0, None),  # TODO Not possible in Gen 5???
    "Level up (female)": EvolutionMethodData(0, lambda value: always_possible),
    "Level up (male)": EvolutionMethodData(0, lambda value: always_possible),
    "Level up with party member": EvolutionMethodData(0, lambda value: has_species(species.by_id[value, 0])),
}
