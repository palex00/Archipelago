from BaseClasses import Location
from .data import FlagLocationData, VarLocationData
from .data.locations import dexsanity, overworld_items, hidden_items, other

name_to_id: dict[str, int] = {
    name: dexsanity.location_table[name].dex_number + 10000 for name in dexsanity.location_table
} | {
    name: overworld_items.location_table[name].flag_id + 20000 for name in overworld_items.location_table
} | {
    name: hidden_items.location_table[name].flag_id + 20000 for name in hidden_items.location_table
} | {
    name: other.location_table[name].flag_id + 20000
    for name in other.location_table if other.location_table[name] is FlagLocationData
} | {
    name: other.location_table[name].var_id + 30000
    for name in other.location_table if other.location_table[name] is VarLocationData
}


class PokemonBWLocation(Location):
    game = "Pokemon Black and White"
