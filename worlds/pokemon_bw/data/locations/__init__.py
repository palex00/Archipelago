from .. import LocationData
from . import dexsanity, hidden_items, npc, overworld_items

all_locations: dict[str, LocationData] = (
    dexsanity.location_table | overworld_items.location_table | hidden_items.location_table | npc.location_table
)
