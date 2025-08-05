from . import main_items, key_items, medicine, tm_hm, berries, badges, seasons
from .. import NoDuplicatesJustViewButDictsOnly

all_berries: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    berries.standard,
    berries.niche,
)

all_key_items: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    key_items.progression,
    key_items.vanilla,
    key_items.useless,
    key_items.special
)

all_main_items: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    main_items.min_once,
    main_items.filler,
    main_items.mail,
    main_items.unused,
)

all_items_dict_view: NoDuplicatesJustViewButDictsOnly = NoDuplicatesJustViewButDictsOnly(
    badges.table,
    berries.standard,
    berries.niche,
    key_items.progression,
    key_items.vanilla,
    key_items.useless,
    key_items.special,
    main_items.min_once,
    main_items.filler,
    main_items.mail,
    main_items.unused,
    medicine.table,
    seasons.table,
    tm_hm.table,
)
