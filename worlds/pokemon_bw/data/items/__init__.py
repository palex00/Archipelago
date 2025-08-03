from . import main_items, key_items, medicine, tm_hm, berries, badges, seasons
from .. import NoDuplicateJustView

all_badges: NoDuplicateJustView = NoDuplicateJustView(badges.table)

all_berries: NoDuplicateJustView = NoDuplicateJustView(
    *berries.standard,
    *berries.niche,
)

all_key_items: NoDuplicateJustView = NoDuplicateJustView(
    *key_items.progression,
    *key_items.vanilla,
    *key_items.useless,
)

all_main_items: NoDuplicateJustView = NoDuplicateJustView(
    *main_items.min_once,
    *main_items.filler,
    *main_items.mail,
    *main_items.unused,
)

all_medicine: NoDuplicateJustView = NoDuplicateJustView(medicine.table)

all_seasons: NoDuplicateJustView = NoDuplicateJustView(seasons.table)

all_tm_hm: NoDuplicateJustView = NoDuplicateJustView(tm_hm.table)

all_items: NoDuplicateJustView = NoDuplicateJustView(
    *badges.table,
    *all_berries,
    *all_key_items,
    *all_main_items,
    *medicine.table,
    *seasons.table,
    *tm_hm.table,
)
