"""
Option definitions for Pokemon Black and White
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup, StartInventory)

from .data import data

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Champion: Become the champion and enter the hall of fame
    - Steven: Defeat Steven in Meteor Falls
    - Norman: Defeat Norman in Petalburg Gym
    - Legendary Hunt: Defeat or catch legendary pokemon (or whatever was randomized into their encounters)
    """
    display_name = "Goal"
    default = 0
    option_champion = 0
    option_steven = 1
    option_norman = 2
    option_legendary_hunt = 3

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