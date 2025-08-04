from BaseClasses import MultiWorld, Item
from worlds.AutoWorld import World
from .generate import SpeciesEntry
from .items import PokemonBWItem, generate_item
from .options import PokemonBWOptions


class PokemonBWWorld(World):
    # TODO EVERYTHING
    options_dataclass = PokemonBWOptions
    options: PokemonBWOptions

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.strength_species: set[str] = None
        self.cut_species: set[str] = None
        self.surf_species: set[str] = None
        self.dive_species: set[str] = None
        self.waterfall_species: set[str] = None
        self.fighting_type_species: set[str] = None  # Needed for challenge rock outside of pinwheel forest

    def create_item(self, name: str) -> Item:
        return generate_item(name, self)
