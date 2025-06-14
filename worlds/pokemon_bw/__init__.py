from BaseClasses import MultiWorld
from worlds.AutoWorld import World
from .generate import SpeciesEntry


class PokemonBWWorld(World):
    # TODO EVERYTHING

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.species_entries: dict[str, SpeciesEntry] = None
        self.strength_species: set[str] = None
        self.cut_species: set[str] = None
        self.surf_species: set[str] = None
        self.dive_species: set[str] = None
        self.waterfall_species: set[str] = None
        self.fighting_type_species: set[str] = None  # Needed for challenge rock outside of pinwheel forest
