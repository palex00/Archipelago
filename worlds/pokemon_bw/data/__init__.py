from typing import NamedTuple, Callable

from BaseClasses import ItemClassification


class ItemData(NamedTuple):
    id: int
    classification: Callable[[PokemonBWOptions], ItemClassification]
