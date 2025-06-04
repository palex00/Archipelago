from dataclasses import dataclass

from Options import (Choice, PerGameCommonOptions, OptionSet, Range, Toggle, OptionCounter)


class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.
    - **Ghetsis** - Clear the main story by defeating Ghetsis
    - **Champion** - Become the champion by defeating Alder
    - **Cynthia** - Defeat Cynthia in Undella Town
    - **Regional pokédex** - Complete the Unova pokédex
    - **National pokédex** - Complete the national pokédex
    - **TM/HM hunt** - Get all TMs and HMs
    - **Seven Sages hunt** - Find the Seven Sages
    """
    display_name = "Goal"
    option_ghetsis = 0
    option_champion = 1
    option_cynthia = 2
    # option_regional_pokedex = 3
    # option_national_pokedex = 4
    option_tmhm_hunt = 5
    option_seven_sages_hunt = 6
    default = 0


class GameVersion(Choice):
    """
    Select your game version.
    """
    display_name = "Game Version"
    option_black = 0
    option_white = 1
    default = "random"


class RandomizeWildPokemon(OptionSet):
    """
    Randomizes wild pokémon encounters.
    - **Randomize** - Toggles wild pokémon being randomized. Required for any other modifier.
    - **Similar base stats** - Tries to keep every randomized pokémon at a similar base stat total as the replaced encounter.
    - **Type themed** - Makes every pokémon in an area have a certain same type.
    - **Area 1-to-1** - Keeps the amount of different encounters and their encounter rate in every area.
    """
    display_name = "Randomize Wild Pokémon"
    valid_keys = [
        "Randomize",
        "Similar base stats",
        "Type themed",
        "Area 1-to-1",
    ]
    default = ["Randomize"]


class RandomizeTrainerPokemon(OptionSet):
    """
    Randomizes trainer pokémon.
    - **Normalize areas** - Decreases the levels of trainers in postgame areas to make those viable for playthroughs.
                            Does not affect Cynthia. Does not require trainer pokémon being randomized.
    - **Randomize** - Toggles trainer pokémon being randomized. Required for any modifier below.
    - **Similar base stats** - Tries to keep the randomized pokémon at a similar base stat total as the replaced one.
    - **Type themed** - All pokémon of a trainer have to share at least one randomly chosen type.
                        Gym leaders will always have themed teams, regardless of this modifier.
    - **Themed gym trainers** - All pokémon of gym trainers will share the type assigned to the gym leader.
    """
    display_name = "Randomize Trainer Pokémon"
    valid_keys = [
        "Normalize areas",
        "Randomize",
        "Similar base stats",
        "Type themed",
        "Themed gym trainers",
    ]
    default = ["Normalize areas", "Randomize", "Themed gym trainers"]


class RandomizeStarterPokemon(OptionSet):
    """
    Randomizes the starter pokémon you receive at the start of the game.
    - **Randomize** - Toggles starter pokémon being randomized. Required for any other modifier.
    - **Any base** - Only use unevolved/baby pokémon.
    - **Base with 2 evolutions** - Only use unevolved/baby pokémon that can evolve twice. Overrides **Any base**.
    - **Type variety** - Every starter will have a single type that is different from the other two.
    """
    display_name = "Randomize Starter Pokémon"
    valid_keys = [
        "Randomize",
        "Any base",
        "Base with 2 evolutions",
        "Type variety",
    ]
    default = ["Randomize"]


class RandomizeStaticPokemon(OptionSet):
    """
    Randomizes static encounters you can battle and catch throughout the game, e.g. Volcarona in Relic Castle.
    - **Randomize** - Toggles static pokémon being randomized. Required for any other modifier.
    - **Similar base stats** - Tries to keep the randomized pokémon at a similar base stat total as the replaced one.
    - **Only base** - Only use unevolved Pokémon.
    - **No legendaries** - Exclude legendaries from being placed into static encounters.
    """
    display_name = "Randomize Static Pokémon"
    valid_keys = [
        "Randomize",
        "Similar base stats",
        "Only base",
        "No legendaries",
    ]
    default = []


class RandomizeGiftPokemon(OptionSet):
    """
    Randomizes gift pokémon that you receive for free, e.g. the Larvesta egg on route 18.
    - **Randomize** - Toggles gift pokémon being randomized. Required for any other modifier.
    - **Similar base stats** - Tries to keep the randomized pokémon at a similar base stat total as the replaced one.
    - **No legendaries** - Exclude legendaries from being placed into gift encounters.
    """
    display_name = "Randomize Gift Pokémon"
    valid_keys = [
        "Randomize",
        "Similar base stats",
        "No legendaries",
    ]
    default = []


class RandomizeTradePokemon(OptionSet):
    """
    Randomizes trade offers from NPCs. Any **Randomize ...** is required for the other modifiers.
    - **Randomize offer** - Toggles offered pokémon being randomized.
    - **Randomize request** - Toggles requested pokémon being randomized.
    - **Similar base stats** - Tries to keep the randomized pokémon at a similar base stat total as the replaced one.
    - **No legendaries** - Exclude legendaries from being placed into trades.
    """
    display_name = "Randomize Trade Pokémon"
    valid_keys = [
        "Randomize offer",
        "Randomize request",
        "Similar base stats",
        "No legendaries",
    ]
    default = []


class RandomizeLegendaryPokemon(OptionSet):
    """
    Randomizes legendary and mythical encounters.
    - **Randomize** - Toggles legendary pokémon being randomized. Required for any other modifier.
    - **Keep legendary** - Randomized pokémon will all still be legendaries or mythicals.
    - **Same type** - Tries to keep at least one type of every encounter.
    """
    display_name = "Randomize Legendary Pokémon"
    valid_keys = [
        "Randomize",
        "Keep legendary",
        "Same type",
    ]
    default = []


class RandomizeBaseStats(OptionSet):
    """
    Randomizes the base stats of every pokémon species.
    - **Randomize** - Toggles base stats being randomized. Required for any other modifier.
    - **Keep total** - Every species will keep the sum of its base stats.
    - **Follow evolutions** - Evolved species will use their pre-evolution's base stats and add on top of that.
    """
    display_name = "Randomize Base Stats"
    valid_keys = [
        "Randomize",
        "Keep total",
        "Follow evolutions",
    ]
    default = []


class BaseStatTotalLimits(OptionCounter):
    """
    Determines the maximum and minimum base stat total if base stats are randomized.

    Maximum cannot be lower than minimum.
    """
    display_name = "Base Stat Total Limits"
    min = 6
    max = 1530
    valid_keys = [
        "minimum",
        "maximum",
    ]
    default = {"minimum": 6, "maximum": 1530}


class RandomizeEvolutions(OptionSet):
    """
    Randomizes the evolutions of every pokémon species.
    - **Randomize** - Toggles evolutions being randomized. Required for any other modifier.
    - **Keep method** - Keeps the method (e.g. levelup, evolution stone, ...) of every evolution.
    - **Follow type** - Pre-evolution and evolved pokémon always share at least one type.
    - **Allow multiple pre-evolutions** - Multiple pokémon species can evolve into the same species.
    - **Allow more or less branches** - Allows all species to be able to evolve into more or less species than before.
    """
    display_name = "Randomize Evolutions"
    valid_keys = [
        "Randomize",
        "Keep method",
        "Follow type",
        "Allow multiple pre-evolutions",
        "Allow more or less branches",
    ]
    default = []


class RandomizeCatchRates(OptionSet):
    """
    Randomizes the catch rate of every pokémon species.
    - **Shuffle** - Gives every species a commonly used catch rate (e.g. 255, 45, 3, ...).
    - **Randomize** - Gives every species a completely random catch rate. Overrides **Shuffle**.
    - **Follow evolutions** - Evolved species will have a catch rate equal to or lower than their pre-evolution(s).
    """
    display_name = "Randomize Catch Rates"
    valid_keys = [
        "Shuffle",
        "Randomize",
        "Follow evolutions",
    ]
    default = []


class CatchRateLimits(OptionCounter):
    """
    Determines the maximum and minimum catch rate if those are randomized.

    Maximum cannot be lower than minimum.
    """
    display_name = "Catch Rate Limits"
    min = 3
    max = 255
    valid_keys = [
        "minimum",
        "maximum",
    ]
    default = {"minimum": 3, "maximum": 255}


class RandomizeLevelUpMovesets(OptionSet):
    """
    Randomizes the moves a pokémon species learns by leveling up.
    - **Randomize** - Toggles level up movesets being randomized. Required for any other modifier.
    - **Keep types** - Randomized moves have either a matching or normal type.
    - **Progressive power** - If a move is learned after another one, it will have an equal or higher base power.
    - **Keep amount** - Keeps the amount of moves a species learns normally.
    - **Keep levels** - If the species learned a move at a certain level, it will still learn something at that level.
    - **Follow evolutions** - Evolved species will have at least 50% of the level up moveset(s)
                              of their pre-evolution(s). Overrides all **Keep ...** modifiers.
    """
    display_name = "Randomize Level Up Movesets"
    valid_keys = [
        "Randomize",
        "Keep types",
        "Progressive power",
        "Keep amount",
        "Keep levels",
        "Follow evolutions",
    ]
    default = []


class RandomizeTypes(OptionSet):
    """
    Randomizes the type(s) of every pokémon species.
    - **Randomize** - Toggles types being randomized. Required for any other modifier.
    - **Only secondary type** - Only randomizes the secondary type of every species and thereby keeps the primary type.
                                Includes removing it. Not compatible with **Only primary type**.
    - **Only primary type** - Only randomizes the primary type of every species and thereby keeps the secondary type
                              (which might be none). Not compatible with **Only secondary type**.
    - **Follow evolutions** - Evolved species will share at least one type with (one of) their pre-evolutions.
    """
    display_name = "Randomize Types"
    valid_keys = [
        "Randomize",
        "Only secondary type",
        "Only primary type",
        "Follow evolutions",
    ]
    default = []


class RandomizeAbilities(OptionSet):
    """
    Randomizes the abilities of every pokémon species.
    - **Randomize** - Toggles abilities being randomized. Required for any other modifier.
    - **One per pokémon** - Gives every species only one ability.
    - **Follow evolutions** - Evolved pokémon will have the abilities of (one of) their pre-evolution(s)..
    - **Include hidden abilities** - Includes hidden abilities being randomized. Note that only a few select pokémon
                                     that originate from these games can have their hidden ability.
    """
    display_name = "Randomize Abilities"
    valid_keys = [
        "Randomize",
        "One per pokémon",
        "Follow evolutions",
        "Include hidden abilities",
    ]
    default = []


class RandomizeGenderRatio(OptionSet):
    """
    Randomizes the gender ratio of every pokémon species.
    - **Shuffle** - Gives every species a commonly used gender ratio (e.g. 50/50, 1 in 8, ...).
    - **Randomize** - Gives every species a completely random gender ratio. Overrides **Shuffle**.
    - **Follow evolutions** - Evolved species will have the same gender ratio as (one of) their pre-evolution(s).
    """
    display_name = "Randomize Gender Ratio"
    valid_keys = [
        "Shuffle",
        "Randomize",
        "Follow evolutions",
    ]
    default = []


class GenderRatioLimits(OptionCounter):
    """
    Determines the maximum and minimum gender ratio if those are randomized.

    Maximum cannot be lower than minimum.

    0 is always female, 255 is always male.
    """
    display_name = "Gender Ratio Limits"
    min = 0
    max = 255
    valid_keys = [
        "minimum",
        "maximum",
    ]
    default = {"minimum": 0, "maximum": 255}


class RandomizeTMHMCompatibility(OptionSet):
    """
    Randomizes the TM and HM compatibility of every pokémon species.
    - **Randomize** - Toggles TM and HM compatibility being randomized. Required for any other modifier.
    - **Keep types** - Randomized moves have either a matching or normal type.
    - **Keep amount** - Keeps the amount of moves a species learns normally.
    - **Follow evolutions** - Evolved species will have at least 50% of the learnable TMs and HMs
                              of their pre-evolution(s). Overrides all **Keep ...** modifiers.
    """
    display_name = "Randomize TM/HM Compatibility"
    valid_keys = [
        "Randomize",
        "Keep types",
        "Keep amount",
        "Follow evolutions",
    ]
    default = []


# randomize_badges: RandomizeBadges
class RandomizeBadges(Choice):
    """
    Randomizes the gym badges and restricts the gym leaders' items.
    - **No** - Gym badges will stay at their vanilla locations.
    - **Shuffle leaders** - Gym badges are shuffled between the gym leaders.
    - **Leaders any badge** - Puts the badges into the item pool, while only allowing items that have the word "badge"
                              in their name being placed at gym leaders.
    - **Anywhere** - Gym badges can be anywhere and gym leaders can have any item.
    """
    display_name = "Randomize Badges"
    option_no = 0
    option_shuffle_leaders = 1
    option_leaders_any_badge = 2
    option_anywhere = 3
    default = 1


class ShuffleRoadblockReqs(Toggle):
    """
    Roadblocks always require a specific item to disappear in this randomizer.
    If set to true, roadblocks will require a random key item.
    """
    display_name = "Shuffle Roadblock Requirements"
    default = False


class AdditionalRoadblocks(Choice):
    """
    Adds a number of additional roadblocks like cut trees or npcs blocking your way across the region.
    """
    display_name = "Additional Roadblocks"
    option_none = 0
    option_some = 1
    option_many = 2
    default = 0


class Dexsanity(Range):
    """
    Adds a number of locations that can be checked by catching a certain Pokémon species
    and registering it in the pokédex.

    Any value higher than 135 requires wild pokémon to be randomized.

    If wild pokémon are not randomized, only unovan pokémon will have dexsanity checks.
    """
    display_name = "Dexsanity"
    default = 0
    range_start = 0
    # range_end = 649
    range_end = 135  # Temporary because of missing wild randomization


class Trainersanity(Range):
    """
    Adds a number of locations that can be checked by defeating a regular trainer.
    """
    display_name = "Trainersanity"
    default = 0
    range_start = 0
    range_end = 1  # TODO need to count viable trainers in the game (e.g. Ghetsis and gym leaders are not viable)


class DoorShuffle(OptionSet):
    """
    Shuffles or randomizes door warps.
    - **Gates** - Shuffles city gate entrances, leading to the region having a different layout than normally.
    - **Buildings per map** - Shuffles the building entrances (not gates) within every city or route.
    - **Buildings anywhere** - Shuffles building entrances (not gates) all over Unova.
    - **Dungeons** - Shuffles the location of all dungeons with two entrances and all dungeons with only one entrance.
    - **Full** - Fully shuffle all door warps. Overrides all modifiers above.
    - **Decoupled** - Removes the requirement for all shuffled door warps leading to each other.
    """
    display_name = "Door Shuffle"
    valid_keys = [
        "Gates",
        "Buildings per map",
        "Buildings anywhere",
        "Dungeons",
        "Full",
        "Decoupled",
    ]
    default = []


class ExpModifier(Range):
    """
    Multiplies the experience received from defeating wild and trainer pokémon.

    The value is in percent, meaning 100 is normal, 200 is double, 50 is half, etc.
    """
    display_name = "Experience Modifier"
    default = 100
    range_start = 10
    range_end = 160


class AllPokemonSeen(Toggle):
    """
    Marks all pokémon in the pokédex as seen (including all forms, except shinies).
    """
    display_name = "All Pokémon Seen"
    default = False


class AddFairyType(Choice):
    """
    Adds the fairy type from the sixth generation games.
    - **No** - Don't add the fairy type.
    - **Only randomized** - If types are randomized, this adds the fairy type to the pool of possible types.
    - **Modify vanilla** - Updates the type combination of all pokémon that received the fairy type in X and Y.
    """
    display_name = "Add Fairy Type"
    option_no = 0
    option_only_randomized = 1
    option_modify_vanilla = 2
    default = 0


class WonderTrade(Toggle):
    """
    Enables pokémon being sent to and received from the datastorage wonder trade protocol.
    """
    display_name = "Wonder Trade"
    default = False


class TrapsProbability(Range):
    """
    Determines the probability of every randomly generated filler item being replaced by a random trap item.
    """
    display_name = "Traps Probability"
    default = 0
    range_start = 0
    range_end = 100


class UselessKeyItems(Toggle):
    """
    Adds all possible key items to the item pool, even if they're useless.
    """
    display_name = "Useless Key Items"
    default = False


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
    # General
    goal: Goal
    version: GameVersion

    # Pokémon encounters
    # randomize_wild_pokemon: RandomizeWildPokemon
    # randomize_trainer_pokemon: RandomizeTrainerPokemon
    # randomize_starter_pokemon: RandomizeStarterPokemon
    # randomize_static_pokemon: RandomizeStaticPokemon
    # randomize_gift_pokemon: RandomizeGiftPokemon
    # randomize_trade_pokemon: RandomizeTradePokemon
    # randomize_legendary_pokemon: RandomizeLegendaryPokemon

    # Pokémon stats
    # randomize_base_stats: RandomizeBaseStats
    # base_stat_total_limits: BaseStatTotalLimits
    # randomize_evolutions: RandomizeEvolutions
    # randomize_catch_rates: RandomizeCatchRates
    # catch_rates_limits: CatchRatesLimits
    # randomize_level_up_movesets: RandomizeLevelUpMovesets
    # randomize_types: RandomizeTypes
    # randomize_abilities: RandomizeAbilities
    # randomize_gender_ratio: RandomizeGenderRatio
    # gender_ratio_limits: GenderRatioLimits
    # randomize_tm_hm_compatibility: RandomizeTMHMCompatibility

    # Items, locations, and progression
    randomize_badges: RandomizeBadges
    # shuffle_roadblock_reqs: ShuffleRoadblockReqs
    # additional_roadblocks: AdditionalRoadblocks
    dexsanity: Dexsanity
    # trainersanity: Trainersanity
    # door shuffle: DoorShuffle

    # Miscellaneous
    # exp_modifier: ExpModifier
    all_pokemon_seen: AllPokemonSeen
    # add_fairy_type: AddFairyType
    # deathlink: DeathLink  # Needs to be imported from base options
    # wonder_trade: WonderTrade
    # traps_percentage: TrapsPercentage
    useless_key_items: UselessKeyItems
    # funny_dialogue: FunnyDialogue
    reusable_tms: ReusableTMs
