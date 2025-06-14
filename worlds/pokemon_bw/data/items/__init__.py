from . import main_items, key_items, medicine, tm_hm, berries, badges
from .. import ItemData

all_bag_item_data: dict[str, ItemData] = (
    main_items.filler_table | main_items.special_table | main_items.unused_table | key_items.item_table |
    medicine.item_table | tm_hm.item_table | berries.item_table
)

all_items: set[str] = {
    name for name in all_bag_item_data
} | {
    name for name in badges.item_table
}
