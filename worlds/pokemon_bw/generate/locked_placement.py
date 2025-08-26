from typing import TYPE_CHECKING

from BaseClasses import Item, Location

if TYPE_CHECKING:
    from .. import PokemonBWWorld


def place_badges(world: "PokemonBWWorld", progitempool: list[Item], fill_locations: list[Location]) -> None:
    from ..data.items import badges
    from ..data.locations.ingame_items import special

    match world.options.shuffle_badges.current_key:
        case "vanilla":
            badge_items: dict[str, Item] = {
                item.name: item
                for item in progitempool
                if item.name in badges.table and item.player == world.player
            }
            badge_locations: dict[str, Location] = {
                loc.name: loc
                for loc in fill_locations
                if loc.name in special.gym_badges and loc.player == world.player
            }
            badge_locations["Striaton Gym - Badge reward"].place_locked_item(badge_items["Trio Badge"])
            badge_locations["Nacrene Gym - Badge reward"].place_locked_item(badge_items["Basic Badge"])
            badge_locations["Castelia Gym - Badge reward"].place_locked_item(badge_items["Insect Badge"])
            badge_locations["Nimbasa Gym - Badge reward"].place_locked_item(badge_items["Bolt Badge"])
            badge_locations["Driftveil Gym - Badge reward"].place_locked_item(badge_items["Quake Badge"])
            badge_locations["Mistralton Gym - Badge reward"].place_locked_item(badge_items["Jet Badge"])
            badge_locations["Icirrus Gym - Badge reward"].place_locked_item(badge_items["Freeze Badge"])
            badge_locations["Opelucid Gym - Badge reward"].place_locked_item(badge_items["Legend Badge"])
            for item in badge_items.values():
                progitempool.remove(item)
            for loc in badge_locations.values():
                fill_locations.remove(loc)
        case "shuffle":
            badge_items: list[Item] = [
                item
                for item in progitempool
                if item.name in badges.table and item.player == world.player
            ]
            badge_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in special.gym_badges and loc.player == world.player
            ]
            for _ in range(min(8, len(badge_items))):
                item = badge_items.pop()
                location = badge_locations.pop()
                location.place_locked_item(item)
                progitempool.remove(item)
                fill_locations.remove(location)
        case "any_badge":
            badge_items: list[Item] = [
                item
                for item in progitempool
                if "badge" in item.name.lower()
            ]
            badge_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in special.gym_badges and loc.player == world.player
            ]
            for _ in range(min(8, len(badge_items))):
                item = badge_items.pop()
                location = badge_locations.pop()
                location.place_locked_item(item)
                progitempool.remove(item)
                fill_locations.remove(location)
        case "anything":
            pass
        case _:
            raise Exception(f"Bad shuffle_badges option value for player {world.player_name}")


def place_tm_hm(world: "PokemonBWWorld",
                progitempool: list[Item],
                usefulitempool: list[Item],
                filleritempool: list[Item],
                fill_locations: list[Location]) -> None:
    from ..data.items import all_tm_hm, tm_hm
    from ..data.locations.ingame_items.special import tm_hm_ncps, gym_tms
    from ..data.locations import all_tm_locations

    match world.options.shuffle_tm_hm.current_key:
        case "shuffle":
            tm_hm_items: list[Item] = [
                item
                for item in progitempool
                if item.name in all_tm_hm and item.player == world.player
            ] + [
                item
                for item in usefulitempool
                if item.name in all_tm_hm and item.player == world.player
            ]
            tm_hm_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in all_tm_locations and loc.player == world.player
            ]
            for location in tm_hm_locations:
                hm_rule = all_tm_locations[location.name].hm_rule
                for item in tm_hm_items:
                    if hm_rule is None or hm_rule(item.name):
                        tm_hm_items.remove(item)
                        location.place_locked_item(item)
                        if item in progitempool:
                            progitempool.remove(item)
                        else:
                            usefulitempool.remove(item)
                        fill_locations.remove(location)
                        break
        case "hm_with_badge":
            tms: list[Item] = []
            hms: list[Item] = []
            for item in progitempool:
                if item.player == world.player:
                    if item.name in tm_hm.hm or "TM70" in item.name:
                        hms.append(item)
                    elif item.name in tm_hm.tm:
                        tms.append(item)
            for item in usefulitempool:
                if item.player == world.player:
                    if item.name in tm_hm.hm or "TM70" in item.name:
                        hms.append(item)
                    elif item.name in tm_hm.tm:
                        tms.append(item)
            hms.append(tms.pop())
            other_tm_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in tm_hm_ncps and loc.player == world.player
            ]
            gym_tm_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in gym_tms and loc.player == world.player
            ]
            for location in gym_tm_locations:
                hm_rule = all_tm_locations[location.name].hm_rule
                for item in hms:
                    if hm_rule is None or hm_rule(item.name):
                        hms.remove(item)
                        location.place_locked_item(item)
                        if item in progitempool:
                            progitempool.remove(item)
                        else:
                            usefulitempool.remove(item)
                        fill_locations.remove(location)
                        break
            for location in other_tm_locations:
                hm_rule = all_tm_locations[location.name].hm_rule
                for item in tms:
                    if hm_rule is None or hm_rule(item.name):
                        tms.remove(item)
                        location.place_locked_item(item)
                        if item in progitempool:
                            progitempool.remove(item)
                        else:
                            usefulitempool.remove(item)
                        fill_locations.remove(location)
                        break
        case "any_tm_hm":
            tm_hm_items: list[Item] = [
                item
                for item in progitempool
                if (item.name.lower().startswith("tm") or item.name.lower().startswith("hm")) and item.name[2].isdigit()
            ] + [
                item
                for item in usefulitempool
                if (item.name.lower().startswith("tm") or item.name.lower().startswith("hm")) and item.name[2].isdigit()
            ] + [
                item
                for item in filleritempool
                if (item.name.lower().startswith("tm") or item.name.lower().startswith("hm")) and item.name[2].isdigit()
            ]
            tm_hm_locations: list[Location] = [
                loc
                for loc in fill_locations
                if loc.name in all_tm_locations and loc.player == world.player
            ]
            for location in tm_hm_locations:
                hm_rule = all_tm_locations[location.name].hm_rule
                for item in tm_hm_items:
                    if hm_rule is None or hm_rule(item.name):
                        tm_hm_items.remove(item)
                        location.place_locked_item(item)
                        if item in progitempool:
                            progitempool.remove(item)
                        else:
                            usefulitempool.remove(item)
                        fill_locations.remove(location)
                        break
        case "anything":
            pass
        case _:
            raise Exception(f"Bad shuffle_tm_hm option value for player {world.player_name}")
