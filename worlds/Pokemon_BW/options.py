"""
Option definitions for Pokemon Black and White
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup)

from .data import data

class GameVersion(Choice):
    """
    Select Black or White version.
    """
    display_name = "Game Version"
    option_black = 0
    option_white = 1
    default = "random"

class goal(Choice):
    """
    Determines what your goal is to consider the game beaten.
    - Champion - Defeat Alder
    - Cynthia - Defeat cynthia
    - Fulldex - Finish the Pokedex
    - TM/HM hunt - Find an amount of TMs and HMs
    - Seven Sages - Find the Seven Sages
    """
    display_name = "Goal"
    default = 0
    option_champion = 0
    option_cynthia = 1
    option_fulldex = 2
    option_tmhm = 3
    option_sages = 4

class Dexsanity(Choice):
    """
    Enables Dexsanity
    """
    display_name = "Dexsanity"
    default = 0
    option_off = 0
    option_on = 1

class FunnyDialogue(Choice):
    """
    Adds humorous dialogue submitted by the folks in the Pokemon Black and White thread of the Archipelago Discord server
    """
    display_name = "FunnyDialogue"
    default = 0
    option_off = 0
    option_on = 1

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

class DeathLink(Choice):
    """
    Toggles DeathLink. (not currently functional)
    """
    display_name = "DeathLink"
    default = 0
    option_off = 0
    option_on = 1