from BaseClasses import LocationProgressType
from ... import PokemonBWWorld
from ...options import PokemonBWOptions


def always_priority(options: PokemonBWOptions, world: PokemonBWWorld) -> LocationProgressType:
    return LocationProgressType.PRIORITY


def always_default(options: PokemonBWOptions, world: PokemonBWWorld) -> LocationProgressType:
    return LocationProgressType.DEFAULT


def always_excluded(options: PokemonBWOptions, world: PokemonBWWorld) -> LocationProgressType:
    return LocationProgressType.EXCLUDED
