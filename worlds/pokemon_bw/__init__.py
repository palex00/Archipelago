import datetime
import os
from typing import ClassVar

import settings
from BaseClasses import MultiWorld, Tutorial
from worlds.AutoWorld import World, WebWorld
from . import items, locations, options, bizhawk_client, rom


bizhawk_client.register_client()


class PokemonBWSettings(settings.Group):

    class PokemonBlackRomFile(settings.UserFilePath):
        """File name of your Pokémon Black Version ROM"""
        description = "Pokemon Black Version ROM"
        copy_to = "PokemonBlack.nds"

    class PokemonWhiteRomFile(settings.UserFilePath):
        """File name of your Pokémon White Version ROM"""
        description = "Pokemon White Version ROM"
        copy_to = "PokemonWhite.nds"

    black_rom: PokemonBlackRomFile = PokemonBlackRomFile(PokemonBlackRomFile.copy_to)
    white_rom: PokemonWhiteRomFile = PokemonWhiteRomFile(PokemonWhiteRomFile.copy_to)



class PokemonBWWeb(WebWorld):
    rich_text_options_doc = True
    theme = ("grassFlowers", "ocean", "dirt", "ice")[(datetime.datetime.now().month - 1) % 4]
    game_info_languages = ["en"]
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pokémon Black and White with Archipelago:",
        "English",
        "setup_en.md",
        "setup/en",
        ["BlastSlimey"]
    )
    tutorials = [setup_en]


class PokemonBWWorld(World):
    """
    Pokémon Black and White are the introduction to the fifth generation of the Pokémon franchise.
    Travel through the Unova region, catch a variety of brand new Pokémon you have never seen before,
    collect the eight gym badges, fight Team Plasma, who claim to be the saviors of all the Pokémon,
    and become the champion of the region.
    These games present themselves in 2.5D graphics,
    while still using the known grid-based movement mechanics and battle UI.
    """
    game = "Pokemon Black and White"
    options_dataclass = options.PokemonBWOptions
    options: options.PokemonBWOptions
    topology_present = True
    web = PokemonBWWeb()
    item_name_to_id = items.get_item_lookup_table()
    location_name_to_id = locations.get_location_lookup_table()
    settings_key = "pokemon_bw_settings"
    settings: ClassVar[PokemonBWSettings]

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.strength_species: set[str] = set()
        self.cut_species: set[str] = set()
        self.surf_species: set[str] = set()
        self.dive_species: set[str] = set()
        self.waterfall_species: set[str] = set()
        self.fighting_type_species: set[str] = set()  # Needed for challenge rock outside of pinwheel forest
        self.to_be_filled_locations: int = 0

    def create_item(self, name: str) -> items.PokemonBWItem:
        return items.generate_item(name, self)

    def get_filler_item_name(self) -> str:
        return items.generate_filler(self)

    def create_regions(self) -> None:
        regions = locations.get_regions(self)
        rules = locations.create_rule_dict(self)
        locations.connect_regions(self, regions, rules)
        locations.cleanup_regions(regions)
        catchable_dex_form = locations.create_and_place_event_locations(self, regions, rules)
        locations.create_and_place_locations(self, regions, rules, catchable_dex_form)
        self.to_be_filled_locations = locations.count_to_be_filled_locations(regions)
        self.multiworld.regions.extend(regions.values())

    def create_items(self) -> None:
        item_pool = items.get_main_item_pool(self)
        items.place_locked_items(self, item_pool)
        if len(item_pool) > self.to_be_filled_locations:
            raise Exception(f"Player {self.player_name} has more guaranteed items than to-be-filled locations."
                            f"Please report this to the maintainer and provide the yaml used for generating.")
        for _ in range(self.to_be_filled_locations-len(item_pool)):
            item_pool.append(self.create_item(self.get_filler_item_name()))
        self.multiworld.itempool += item_pool

    def generate_output(self, output_directory: str) -> None:
        if self.options.version == "black":
            rom.PokemonBlackPatch(
                path=os.path.join(
                    output_directory,
                    self.multiworld.get_out_file_name_base(self.player) + rom.PokemonBlackPatch.patch_file_ending
                ), world=self, player=self.player, player_name=self.player_name
            ).write()
        else:
            rom.PokemonWhitePatch(
                path=os.path.join(
                    output_directory,
                    self.multiworld.get_out_file_name_base(self.player) + rom.PokemonWhitePatch.patch_file_ending
                ), world=self, player=self.player, player_name=self.player_name
            ).write()
