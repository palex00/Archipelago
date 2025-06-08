from typing import NamedTuple, Callable, Literal

from BaseClasses import ItemClassification, LocationProgressType, CollectionState
from ..options import PokemonBWOptions


class ItemData(NamedTuple):
    id: int
    # Takes the options and extra data and returns the classification (progression, useful, filler, or trap)
    # for the calling world
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]
    bag: Literal["Main", "Key", "Medicine", "Berries", "TM/HM"]


class BadgeItemData(NamedTuple):
    bit: int
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]


class LocationData(NamedTuple):
    address_black: int
    address_white: int
    # Takes the read value, does something with it (e.g. check for value or certain bit)
    # and returns whether the location was checked
    checking_type: Callable[[int], bool]
    # Takes the options and extra data and returns the progress type (NORMAL, PRIORITY, or EXCLUDED)
    # for the calling world
    progress_type: Callable[[PokemonBWOptions, dict[str, any]], LocationProgressType]
    region: str
    # An extra rule that is not covered by region access (e.g. items behind a strength boulder)
    rule: Callable[[CollectionState], bool] | None


class EncounterData(NamedTuple):
    # (dex number, form)
    species_black: tuple[int, int]
    species_white: tuple[int, int]
    encounter_region: str
    # The following will become important when wild encounter randomization happens
    # file_number: int
    # offset: int


class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: Callable[[CollectionState], bool] | None


class SpeciesData(NamedTuple):
    dex_number: int
    form: int
    type_1: str
    type_2: str
    base_hp: int
    base_attack: int
    base_defense: int
    base_sp_attack: int
    base_sp_defense: int
    base_speed: int
    catch_rate: int
    gender_ratio: int
    # starts with 0 for base evolutions
    evolution_stage: int
    # (primary, secondary, hidden)
    abilities: tuple[str, str, str]
    # tuple(method, parameter, evolve into)
    evolutions: list[tuple[str, int, str]]


class MovesetData(NamedTuple):
    # tuple(level, move name)
    level_up_moves: list[tuple[int, str]]
    # TM number (101+ are HMs)
    tm_hm_moves: set[int]


class MoveData(NamedTuple):
    type: str
    category: Literal["Physical", "Special", "Status"]
    power: int
    # (Number of positive effects) - (Number of negative effects)
    effects_difference: int
    pp: int


class TMHMData(NamedTuple):
    move: str
    is_HM: bool


class EvolutionMethodData(NamedTuple):
    id: int
    # The access rule for dexsanity logic
    rule: Callable[[CollectionState], bool]


class TypeData(NamedTuple):
    id: int
