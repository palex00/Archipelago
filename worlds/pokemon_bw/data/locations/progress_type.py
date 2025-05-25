from BaseClasses import LocationProgressType
from ...options import PokemonBWOptions


def always_priority(options: PokemonBWOptions, data: dict[str, any]) -> LocationProgressType:
    return LocationProgressType.PRIORITY


def always_default(options: PokemonBWOptions, data: dict[str, any]) -> LocationProgressType:
    return LocationProgressType.DEFAULT


def always_excluded(options: PokemonBWOptions, data: dict[str, any]) -> LocationProgressType:
    return LocationProgressType.EXCLUDED
