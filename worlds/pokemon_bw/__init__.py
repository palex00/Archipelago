from BaseClasses import MultiWorld, Item
from worlds.AutoWorld import World
from .client import register_client
from .items import generate_item
from .options import PokemonBWOptions


register_client()


class PokemonBWWorld(World):
    # TODO EVERYTHING
    options_dataclass = PokemonBWOptions
    options: PokemonBWOptions

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.strength_species: set[str] = set()
        self.cut_species: set[str] = set()
        self.surf_species: set[str] = set()
        self.dive_species: set[str] = set()
        self.waterfall_species: set[str] = set()
        self.fighting_type_species: set[str] = set()  # Needed for challenge rock outside of pinwheel forest

    def create_item(self, name: str) -> Item:
        return generate_item(name, self)
