from typing import NamedTuple, Callable

from BaseClasses import ItemClassification, LocationProgressType
from ..options import PokemonBWOptions


class ItemData(NamedTuple):
    id: int
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]


class BadgeItemData(NamedTuple):
    bit: int
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]


class LocationData(NamedTuple):
    address_black: int
    address_white: int
    checking_type_black: Callable[[int], bool]
    checking_type_white: Callable[[int], bool]
    progress_type: Callable[[PokemonBWOptions, dict[str, any]], LocationProgressType]
    region: str
