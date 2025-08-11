from . import dexsanity, regions, region_connections
from .encounters import regions as encounter_regions, slots, static, region_connections as encounter_region_connections
from .ingame_items import overworld_items, hidden_items, other, special
from .. import NoDuplicatesJustViewButDictsOnly

all_region_connections: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    region_connections.connections,
    encounter_region_connections.connections
)

all_locations: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
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
    static.fossils,
    static.trade,
)

all_item_locations: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    overworld_items.table,
    hidden_items.table,
    other.table,
    special.gym_badges,
    special.tm_hm_ncps,
)
