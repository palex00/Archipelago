from BaseClasses import Item
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from BaseClasses import MultiWorld


def sort_badges(multiworld: "MultiWorld", progitempool: list[Item]) -> None:
    from .. import PokemonBWWorld

    # Look through all worlds and return if none of them have shuffle_badges set to any_badge
    for world in multiworld.worlds.values():
        if isinstance(world, PokemonBWWorld):
            if world.options.shuffle_badges == "any_badge":
                break
    else:
        return

    to_place = 0
    step = 1
    for to_check in range(1, len(progitempool)):
        if "badge" in progitempool[to_check].name.lower():
            progitempool[to_place], progitempool[to_check] = progitempool[to_check], progitempool[to_place]
            to_place = min(to_place + step, to_check)
            step = 2 if step == 1 else 1


def sort_tm_hm(multiworld: "MultiWorld", progitempool: list[Item], usefulitempool: list[Item]) -> None:
    from .. import PokemonBWWorld

    # Look through all worlds and return if none of them have shuffle_badges set to any_badge
    for world in multiworld.worlds.values():
        if isinstance(world, PokemonBWWorld):
            if world.options.shuffle_tm_hm == "any_tm_hm":
                break
    else:
        return

    for pool in (progitempool, usefulitempool):
        to_place = 0
        step = 1
        for to_check in range(1, len(pool)):
            if (
                (pool[to_check].name.lower().startswith("tm") or pool[to_check].name.lower().startswith("hm"))
                and len(pool[to_check].name) > 2 and pool[to_check].name[2].isdigit()
            ):
                pool[to_place], pool[to_check] = pool[to_check], pool[to_place]
                to_place = min(to_place + step, to_check)
                step = 2 if step == 1 else 1
