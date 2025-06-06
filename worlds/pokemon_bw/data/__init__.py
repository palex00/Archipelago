from typing import NamedTuple, Callable, Literal

from BaseClasses import ItemClassification, LocationProgressType, CollectionState
from ..options import PokemonBWOptions


class ItemData(NamedTuple):
    id: int
    # Takes the options and extra data and returns the classification (progression, useful, filler, or trap) for the calling world
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]
    bag: Literal["Main", "Key", "Medicine", "Berries", "TM/HM"]


class BadgeItemData(NamedTuple):
    bit: int
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]


class LocationData(NamedTuple):
    address_black: int
    address_white: int
    # Takes the address, does something with it (e.g. check for value or certain bit) and returns whether the location was checked
    checking_type: Callable[[int], bool]
    # Takes the options and extra data and returns the progress type (NORMAL, PRIORITY, or EXCLUDED) for the calling world
    progress_type: Callable[[PokemonBWOptions, dict[str, any]], LocationProgressType]
    region: str
    # An extra rule that is not covered by region access (e.g. items behind a strength boulder)
    rule: Callable[[CollectionState], bool] | None


class EncounterEventData(NamedTuple):
    species_black: str
    species_white: str
    encounter_region: str


class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: Callable[[CollectionState], bool] | None


class SpeciesData(NamedTuple):
    id: int
    type_1: str
    type_2: str
    catch_rate: int
    base_hp: int
    base_attack: int
    base_defense: int
    base_sp_attack: int
    base_sp_defense: int
    base_speed: int
    gender_ratio: int
    level_up_moves: list[tuple[int, str]]
    tm_hm_moves: list[int]


class MoveData(NamedTuple):
    type: str
    category: Literal["Physical", "Special"]
    power: int
    # (Number of positive effects) - (Number of negative effects)
    effects_difference: int
    ap: int


class TMHMData(NamedTuple):
    move: str
    is_HM: bool
