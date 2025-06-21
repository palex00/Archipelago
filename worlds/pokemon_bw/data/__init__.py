from typing import NamedTuple, Callable, Literal

from BaseClasses import ItemClassification, LocationProgressType, CollectionState
from .. import PokemonBWWorld
from ..options import PokemonBWOptions


ExtendedRule: type = Callable[[CollectionState, PokemonBWWorld], bool]
ClassificationMethod: type = Callable[[PokemonBWOptions, PokemonBWWorld], ItemClassification]
ProgressTypeMethod: type = Callable[[PokemonBWOptions, PokemonBWWorld], LocationProgressType]


class ItemData(NamedTuple):
    id: int
    # Takes the options and extra data and returns the classification (progression, useful, filler, or trap)
    # for the calling world
    classification: ClassificationMethod
    bag: Literal["Main", "Key", "Medicine", "Berries", "TM/HM"]


class BadgeItemData(NamedTuple):
    bit: int
    classification: ClassificationMethod


class FlagLocationData(NamedTuple):
    # flags begin at 0x23bf28 (B) or 0x23bf48 (W)
    flag_id: int
    progress_type: ProgressTypeMethod
    region: str
    rule: ExtendedRule | None


class VarLocationData(NamedTuple):
    # global variables begin at 0x23bd30 (B) or 0x23bd50 (W)
    # global vars 0x4000-0x4081 have 1 byte, 0x4082+ have 2 bytes
    var_id: int
    checking_type: Callable[[int], bool]
    progress_type: ProgressTypeMethod
    region: str
    rule: ExtendedRule | None


class DexLocationData(NamedTuple):
    # caught flags are stored at 0x23D1B4 (B) or 0x23D1D4 (W)
    dex_number: int
    # Use special rule if there are more than one species for a dex entry (e.g. Wormadam, Deoxys, Castform, ...)
    special_rule: ExtendedRule | None = None


"""class LocationData(NamedTuple):
    # Just choose any number between 0 and 9999 for each location in a table
    custom_id: int
    address_black: int
    address_white: int
    # Takes the read value, does something with it (e.g. check for value or certain bit)
    # and returns whether the location was checked
    checking_type: Callable[[int], bool]
    # Takes the options and extra data and returns the progress type (NORMAL, PRIORITY, or EXCLUDED)
    # for the calling world
    progress_type: Callable[[PokemonBWOptions, dict[str, any]], LocationProgressType]
    region: str
    # An extra rule that is not covered by region access (e.g. items behind a strength boulder)
    #
    rule: ExtendedRule | None"""


class EncounterData(NamedTuple):
    # (dex number, form)
    species_black: tuple[int, int]
    species_white: tuple[int, int]
    encounter_region: str
    exclude_logic: bool
    # The following will become important when wild encounter randomization happens
    # file_number: int
    # offset: int


class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: ExtendedRule | None


class SpeciesData(NamedTuple):
    dex_name: str
    dex_number: int
    form: int
    type_1: str
    type_2: str
    base_hp: int
    base_attack: int
    base_defense: int
    base_sp_attack: int
    base_sp_defense: int
    base_speed: int
    catch_rate: int
    gender_ratio: int
    # starts with 0 for base evolutions
    evolution_stage: int
    # (primary, secondary, hidden)
    abilities: tuple[str, str, str]
    # tuple(method, parameter, evolve into)
    evolutions: list[tuple[str, int, str]]


class MovesetData(NamedTuple):
    # tuple(level, move name)
    level_up_moves: list[tuple[int, str]]
    # TM number (internal order is TM1-95 HM1-6)
    tm_hm_moves: set[str]


# TODO future update
class MoveData(NamedTuple):
    type: str
    category: Literal["Physical", "Special", "Status"]
    power: int
    # (Number of positive effects) - (Number of negative effects)
    effects_difference: int
    pp: int


# TODO future update
class TMHMData(NamedTuple):
    move: str
    is_HM: bool


class EvolutionMethodData(NamedTuple):
    id: int
    # Some evolution methods don't trigger on certain gender, iv, ...
    # Placing species with such an evo method into static encounters could thereby lead to logic errors
    static_allowed: bool
    # Takes value from evolution data and the player id and returns the access rule for that evolution
    rule: Callable[[int], ExtendedRule] | None


# TODO future update
class TypeData(NamedTuple):
    id: int
