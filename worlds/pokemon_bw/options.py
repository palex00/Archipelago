"""
Option definitions for Pokemon Black and White
"""
from dataclasses import dataclass

from Options import (Choice, PerGameCommonOptions, OptionSet, Range, Toggle)


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.
    - **Ghetsis** - Clear the main story by defeating Ghetsis
    - **Champion** - Become the champion by defeating Alder
    - **Cynthia** - Defeat Cynthia in Undella Town
    - **Full pokédex** - Complete the pokédex
    - **TM/HM hunt** - Get all TMs and HMs
    - **Seven Sages hunt** - Find the Seven Sages
    """
    display_name = "Goal"
    default = 0
    option_ghetsis = 0
    option_champion = 1
    option_cynthia = 2
    option_full_pokedex = 3
    option_tmhm_hunt = 4
    option_seven_sages_hunt = 5


class GameVersion(Choice):
    """
    Select your version.
    """
    display_name = "Game Version"
    option_black = 0
    option_white = 1
    default = "random"


class RandomizeWildPokemon(OptionSet):
    """
    Randomizes wild Pokémon encounters.
    - **Randomize** - Toggles wild Pokémon being randomized. Required for any other modifier.
    - **Similar base stats** - Tries to keep the randomized Pokémon at a similar base stat total as the vanilla encounter.
    - **Type themed** - Makes every Pokémon in an area have a certain same type.
    - **Keep variety** - Keeps the amount of different encounters and their encounter rate in every area.
    """
    display_name = "Randomize Wild Pokémon"
    valid_keys = [
        "Randomize",
        "Similar base stats",
        "Type themed",
        "Keep variety",
    ]


class RandomizeStarterPokemon(OptionSet):
    """
    Randomizes the starter Pokémon you receive at the start of the game.
    - **Randomize** - Toggles Starter Pokémon being randomized. Required for any other modifier.
    - **Any base** - Only use unevolved Pokémon.
    - **Base with 2 evolutions** - Only use unevolved Pokémon that can evolve twice. Overrides **Any base**.
    - **Type variety** - Every starter will have a single type that is different from the other two.
    """
    display_name = "Randomize Starter Pokémon"
    valid_keys = [
        "Randomize",
        "Any base",
        "Base with 2 evolutions",
        "Type variety",
    ]


class Dexsanity(Range):
    """
    Adds a number of locations that can be checked by catching a certain Pokémon species
    """
    display_name = "Dexsanity"
    default = 0
    range_start = 0
    range_end = 649


class FunnyDialogue(Toggle):
    """
    Adds humorous dialogue submitted by the folks in the Pokèmon Black and White thread of the Archipelago Discord server
    """
    display_name = "FunnyDialogue"
    default = 0


class ReusableTMs(Choice):
    """
    Enables reusable TMs, allowing for the reuse of TMs
    """
    display_name = "ReusableTMs"
    default = 0
    option_on = 0
    option_yes = 1
    option_of_course = 2
    option_im_not_a_masochist = 3


@dataclass
class PokemonBWOptions(PerGameCommonOptions):
    goal: Goal
    version: GameVersion
    randomize_wild_pokemon: RandomizeWildPokemon
    randomize_starter_pokemon: RandomizeStarterPokemon
    dexsanity: Dexsanity
    funny_dialogue: FunnyDialogue
    reusable_tms: ReusableTMs
