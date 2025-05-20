from typing import NamedTuple, Callable

from BaseClasses import ItemClassification
from ..options import PokemonBWOptions


class ItemData(NamedTuple):
    id: int
    classification: Callable[[PokemonBWOptions, dict[str, any]], ItemClassification]
