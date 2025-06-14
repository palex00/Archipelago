from BaseClasses import Item
from .data.items import all_bag_item_data, badges

name_to_id: dict[str, int] = {
    name: all_bag_item_data[name].id for name in all_bag_item_data
} | {
    name: badges.item_table[name].bit + 1000 for name in badges.item_table
}


class PokemonBWItem(Item):
    game = 'Pokemon Black and White'
