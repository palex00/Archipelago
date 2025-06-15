from .. import VarLocationData, FlagLocationData
from . import dexsanity
from .ingame_items import (overworld_items_south, overworld_items_west, hidden_items_south, hidden_items_west,
                           other_south, other_west)

all_locations: dict[str, VarLocationData | FlagLocationData] = (
    dexsanity.location_table
    | overworld_items_south.table | overworld_items_west.table
    | hidden_items_south.table | hidden_items_west.table
    | other_south.table | other_west.table
)
