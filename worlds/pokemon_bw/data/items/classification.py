from typing import Callable

from BaseClasses import ItemClassification
from ...options import PokemonBWOptions


def always_progression(options: PokemonBWOptions, data: dict[str, any]) -> ItemClassification:
    return ItemClassification.progression


def always_useful(options: PokemonBWOptions, data: dict[str, any]) -> ItemClassification:
    return ItemClassification.useful


def always_filler(options: PokemonBWOptions, data: dict[str, any]) -> ItemClassification:
    return ItemClassification.filler


def always_trap(options: PokemonBWOptions, data: dict[str, any]) -> ItemClassification:
    return ItemClassification.trap
