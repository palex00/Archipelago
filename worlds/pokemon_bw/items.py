from random import Random
from typing import TYPE_CHECKING, Any

from BaseClasses import Item

if TYPE_CHECKING:
    from . import PokemonBWWorld
    from .data import NoDuplicatesJustViewButDictsOnly
    all_items_dict_view: NoDuplicatesJustViewButDictsOnly | None = None
else:
    all_items_dict_view = None


class PokemonBWItem(Item):
    game = 'Pokemon Black and White'


def generate_item(name: str, world: "PokemonBWWorld") -> PokemonBWItem:
    global all_items_dict_view

    if all_items_dict_view is None:
        from .data.items import all_items_dict_view as imported
        all_items_dict_view = imported

    data = all_items_dict_view[name]
    # Item id from lookup table is used instead of id from data for safety purposes
    return PokemonBWItem(name, data.classification(world), world.item_name_to_id[name], world.player)


def get_item_lookup_table() -> dict[str, int]:
    from .data.items import badges, berries, key_items, main_items, medicine, seasons, tm_hm

    return ({name: data.item_id for name, data in badges.table.items()} |
            {name: data.item_id for name, data in berries.standard.items()} |
            {name: data.item_id for name, data in berries.niche.items()} |
            {name: data.item_id for name, data in key_items.progression.items()} |
            {name: data.item_id for name, data in key_items.vanilla.items()} |
            {name: data.item_id for name, data in key_items.useless.items()} |
            {name: data.item_id for name, data in key_items.special.items()} |
            {name: data.item_id for name, data in main_items.min_once.items()} |
            {name: data.item_id for name, data in main_items.fossils.items()} |
            {name: data.item_id for name, data in main_items.filler.items()} |
            {name: data.item_id for name, data in main_items.mail.items()} |
            {name: data.item_id for name, data in main_items.unused.items()} |
            {name: data.item_id for name, data in medicine.table.items()} |
            {name: data.item_id for name, data in seasons.table.items()} |
            {name: data.item_id for name, data in tm_hm.table.items()})


def get_main_item_pool(world: "PokemonBWWorld") -> list[PokemonBWItem]:
    from .generate.items import badges, key_items, main_items, seasons, tm_hm

    return (badges.generate_default(world) +
            key_items.generate_default(world) +
            main_items.generate_default(world) +
            seasons.generate_default(world) +
            tm_hm.generate_default(world))


def generate_filler(world: "PokemonBWWorld") -> str:
    from .data.items import berries, main_items, medicine

    main_nested = [
        main_items.filler,
        main_items.filler,
        main_items.filler if "Useful filler" not in world.options.modify_item_pool else [
            main_items.filler,
            main_items.min_once,
            main_items.min_once,
        ],
        main_items.filler if "Ban bad filler" in world.options.modify_item_pool else [
            main_items.filler,
            main_items.filler,
            main_items.filler,
            main_items.mail,
        ],
    ]
    berries_nested = [
        berries.standard,
        berries.standard,
        berries.standard,
        berries.niche,
    ]

    return random_choice_nested(
        world.random, [
            main_nested,
            main_nested,
            berries_nested,
            medicine.table,
            medicine.table,
        ]
    )


def random_choice_nested(random: Random, nested: list[str | list | dict]) -> Any:
    """Helper function for getting a random element from a nested list."""
    current: str | list | dict = nested
    while isinstance(current, list | dict):
        if isinstance(current, list):
            current = random.choice(current)
        else:
            current = random.choice(tuple(current.keys()))
    return current


def place_locked_items(world: "PokemonBWWorld", items: list[PokemonBWItem]) -> None:
    from .generate.locked_placement import place_tm_hm, place_badges, starting_season

    place_tm_hm(world, items)
    place_badges(world, items)
    starting_season(world, items)
