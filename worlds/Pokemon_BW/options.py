"""
Option definitions for Pokemon Black and White
"""
from dataclasses import dataclass

from Options import (Choice, DeathLink, DefaultOnToggle, OptionSet, NamedRange, Range, Toggle, FreeText,
                     PerGameCommonOptions, OptionGroup)


class GameVersion(Choice):
    """
    Select Black or White version.
    """
    display_name = "Game Version"
    option_black = 0
    option_white = 1
    default = "random"

class goal_flag(Choice):
    """
    Determines what your goal is to consider the game beaten.
    - Champion: Become the champion and enter the hall of fame
    - Gym Challenge: Collect all 8 Gym Badges
    """
    display_name = "Goal Flag"
    default = 0
    option_champion = 0
    option_gym_challenge = 1

