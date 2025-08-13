from test.bases import WorldTestBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.pokemon_bw import PokemonBWWorld


class PokemonBWTestBase(WorldTestBase):
    game = "Pokemon Black and White"
    world: "PokemonBWWorld"


# Options irrelevant for testing:
# version (always random)
# reusable_tms (too powerful to test)

# Options that are already included in default options:
# goal: ghetsis
# shuffle_badges: shuffle
# shuffle_tm_hm: shuffle
# dexsanity: 0
# season_control: vanilla
# modify_item_pool: []

# Options that have high failure rate in single worlds:
# shuffle_badges: any_badge


class TestGoalChampion(PokemonBWTestBase):
    options = {"goal": "champion"}


class TestGoalCynthia(PokemonBWTestBase):
    options = {"goal": "cynthia"}


class TestGoalTMHMHunt(PokemonBWTestBase):
    options = {"goal": "tmhm_hunt"}


class TestGoalSevenSagesHunt(PokemonBWTestBase):
    options = {"goal": "seven_sages_hunt"}


class TestShuffleBadgesVanilla(PokemonBWTestBase):
    options = {"shuffle_badges": "vanilla"}


class TestShuffleBadgesAnything(PokemonBWTestBase):
    options = {"shuffle_badges": "anything"}


class TestShuffleTMHMAnyTMHM(PokemonBWTestBase):
    options = {"shuffle_tm_hm": "any_tm_hm"}


class TestShuffleTMHMAnything(PokemonBWTestBase):
    options = {"shuffle_tm_hm": "anything"}


class TestDexsanityPartial(PokemonBWTestBase):
    options = {"dexsanity": 100}


class TestDexsanityFull(PokemonBWTestBase):
    options = {"dexsanity": 649}


class TestSeasonControlChangeable(PokemonBWTestBase):
    options = {"season_control": "changeable"}


class TestSeasonControlRandomized(PokemonBWTestBase):
    options = {"season_control": "randomized"}


class TestModifyItemPoolAll(PokemonBWTestBase):
    options = {"modify_item_pool": ["Useless key items", "Useful filler", "Ban bad filler"]}
