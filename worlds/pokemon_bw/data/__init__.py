from typing import NamedTuple, Callable, Literal, Iterator, Collection, TYPE_CHECKING, TypeVar, Any

from BaseClasses import ItemClassification, LocationProgressType, CollectionState

if TYPE_CHECKING:
    from .. import PokemonBWWorld
    ExtendedRule: type = Callable[[CollectionState, PokemonBWWorld], bool]
    ClassificationMethod: type = Callable[[PokemonBWWorld], ItemClassification]
    ProgressTypeMethod: type = Callable[[PokemonBWWorld], LocationProgressType]
    InclusionRule: type = Callable[[PokemonBWWorld], bool]
    RulesDict: type = dict[ExtendedRule, Callable[[CollectionState], bool]]
else:
    ExtendedRule: type = Any
    ClassificationMethod: type = Any
    ProgressTypeMethod: type = Any
    InclusionRule: type = Any
    RulesDict: type = Any

T = TypeVar("T")
U = TypeVar("U")


class ItemData(NamedTuple):
    item_id: int
    classification: ClassificationMethod


class BadgeItemData(NamedTuple):
    item_id: int
    bit: int
    classification: ClassificationMethod


class SeasonItemData(NamedTuple):
    item_id: int
    flag_id: int
    var_value: int
    classification: ClassificationMethod


class FlagLocationData(NamedTuple):
    # flags begin at 0x23bf28 (B) or 0x23bf48 (W)
    flag_id: int
    progress_type: ProgressTypeMethod
    region: str
    rule: ExtendedRule | None


class DexLocationData(NamedTuple):
    # caught flags are stored at 0x23D1B4 (B) or 0x23D1D4 (W)
    dex_number: int
    # Use special rule if there are more than one species for a dex entry (e.g. Wormadam, Deoxys, Castform, ...)
    special_rule: ExtendedRule | None = None


class EncounterData(NamedTuple):
    # (dex number, form)
    species_black: tuple[int, int]
    species_white: tuple[int, int]
    encounter_region: str
    # The following will become important when wild encounter randomization happens
    # offset: int


class StaticEncounterData(NamedTuple):
    # (dex number, form)
    species_black: tuple[int, int]
    species_white: tuple[int, int]
    encounter_region: str
    inclusion_rule: InclusionRule | None
    access_rule: ExtendedRule | None


class TradeEncounterData(NamedTuple):
    # (dex number, form)
    species_black: tuple[int, int]
    species_white: tuple[int, int]
    # only dex number
    wanted_black: int
    wanted_white: int
    encounter_region: str


class RegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: ExtendedRule | None


class EncounterRegionConnectionData(NamedTuple):
    exiting_region: str
    entering_region: str
    rule: ExtendedRule | None
    inclusion_rule: InclusionRule | None  # None means always included
    # The following will become important when wild encounter randomization happens
    # file_number: int


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
    # Takes value from evolution data and returns the access rule for that evolution
    rule: Callable[[int], ExtendedRule] | None


# TODO future update
class TypeData(NamedTuple):
    id: int


class NoDuplicateJustView(Collection[Collection[T]]):

    def __init__(self, coll1: Collection[T], *collections: Collection[T]):
        self.tup: tuple = (coll1, *collections)

    def __len__(self) -> int:
        return sum((len(x) for x in self.tup))

    def __contains__(self, __x) -> bool:
        for x in self.tup:
            if __x in x:
                return True
        return False

    def __iter__(self):
        return NowINeedAnIterator(self)


class NowINeedAnIterator(Iterator[T]):

    def __init__(self, view: NoDuplicateJustView[T]):
        self.v: NoDuplicateJustView[T] = view
        self.i_outer = 0
        self.i_inner = -1
        self.inner_iterator = iter(view.tup[0])

    def __iter__(self) -> Iterator[T]:
        return NowINeedAnIterator(self.v)

    def __next__(self) -> T:
        self.i_inner += 1
        inner_len = len(self.v.tup[self.i_outer])
        if self.i_inner < inner_len:
            return next(self.inner_iterator)
        elif self.i_inner == inner_len:
            self.i_inner = -1
            self.i_outer += 1
            if self.i_outer < len(self.v.tup):
                self.inner_iterator = iter(self.v.tup[self.i_outer])
                return next(self)
            elif self.i_outer == len(self.v.tup):
                raise StopIteration
            else:  # self.i_outer > len(self.v.tup)
                raise Exception("Something went terribly wrong in the custom iterator")
        else:  # self.i_inner > inner_len
            raise Exception("Something went terribly wrong in the custom iterator")


class NoDuplicatesJustViewButDictsOnly:
    """Very simple view that saves memory, but cannot handle duplicates"""

    def __init__(self, d1: dict, *d: dict):
        self.tup: tuple[dict, any] = (d1, *d)

    def __getitem__(self, key):
        for d in self.tup:
            if key in d:
                return d[key]
        raise KeyError

    def __contains__(self, key) -> bool:
        for d in self.tup:
            if key in d:
                return True
        return False
