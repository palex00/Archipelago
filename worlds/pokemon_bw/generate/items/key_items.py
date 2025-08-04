from typing import TYPE_CHECKING
from ...items import PokemonBWItem

if TYPE_CHECKING:
    from ... import PokemonBWWorld


def generate_default(world: PokemonBWWorld) -> list[PokemonBWItem]:
    from ...data.items.key_items import progression, vanilla, useless

    items = [
        PokemonBWItem(name, data.classification(world), data.item_id, world.player)
        for name, data in progression.items()
    ] + [
        PokemonBWItem(name, data.classification(world), data.item_id, world.player)
        for name, data in vanilla.items()
    ]

    if "Useless key items" in world.options.modify_item_pool:
        items += [
            PokemonBWItem(name, data.classification(world), data.item_id, world.player)
            for name, data in useless.items()
        ]

    return items
