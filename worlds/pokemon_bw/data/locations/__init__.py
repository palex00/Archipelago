from .. import NoDuplicateJustView
from . import dexsanity, regions, region_connections
from .encounters import regions as encounter_regions, slots, static, region_connections as encounter_region_connections
from .ingame_items import overworld_items, hidden_items, other, special

all_regions: NoDuplicateJustView = NoDuplicateJustView(
    regions.region_list,
    encounter_regions.table,
)

all_region_connections: NoDuplicateJustView = NoDuplicateJustView(
    region_connections.connections,
    encounter_region_connections.connections
)

all_locations: NoDuplicateJustView = NoDuplicateJustView(
    overworld_items.table,
    hidden_items.table,
    other.table,
    special.gym_badges,
    special.tm_hm_ncps,
    dexsanity.location_table,
    slots.table,
    static.static,
    static.legendary,
    static.gift,
    static.trade,
)

all_item_locations: NoDuplicateJustView = NoDuplicateJustView(
    overworld_items.table,
    hidden_items.table,
    other.table,
    special.gym_badges,
    special.tm_hm_ncps,
)
