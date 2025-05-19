import struct

from BaseClasses import ItemClassification, Item, IntFlag
import typing
from typing import Dict

progression = ItemClassification.progression
filler = ItemClassification.filler
useful = ItemClassification.useful
trap = ItemClassification.trap


class PkMnBW(Item):
    game = 'Pokemon Black and White'


class ItemData(typing.NamedTuple):
    classification: ItemClassification
    PkMnBWamount: int
    PkMnBWaddress: int

item_table: Dict[str, ItemData] = {
}