from typing import TYPE_CHECKING, Callable

from BaseClasses import Item

if TYPE_CHECKING:
    from .. import PokemonBWWorld
    from ..items import PokemonBWItem


def place_badges(world: "PokemonBWWorld", items: list["PokemonBWItem"]) -> None:
    from ..data.items import badges

    match world.options.shuffle_badges.current_key:
        case "vanilla":
            badge_items: dict[str, "PokemonBWItem"] = {
                item.name: item for item in items if item.name in badges.table
            }
            world.get_location("Striaton Gym - Badge reward").place_locked_item(badge_items["Trio Badge"])
            world.get_location("Nacrene Gym - Badge reward").place_locked_item(badge_items["Basic Badge"])
            world.get_location("Castelia Gym - Badge reward").place_locked_item(badge_items["Insect Badge"])
            world.get_location("Nimbasa Gym - Badge reward").place_locked_item(badge_items["Bolt Badge"])
            world.get_location("Driftveil Gym - Badge reward").place_locked_item(badge_items["Quake Badge"])
            world.get_location("Mistralton Gym - Badge reward").place_locked_item(badge_items["Jet Badge"])
            world.get_location("Icirrus Gym - Badge reward").place_locked_item(badge_items["Freeze Badge"])
            world.get_location("Opelucid Gym - Badge reward").place_locked_item(badge_items["Legend Badge"])
            world.to_be_filled_locations -= 8
            for item in badge_items.values():
                items.remove(item)
        case "shuffle":
            shuffled_list: list["PokemonBWItem"] = [
                item for item in items if item.name in badges.table
            ]
            world.random.shuffle(shuffled_list)
            world.get_location("Striaton Gym - Badge reward").place_locked_item(shuffled_list[0])
            world.get_location("Nacrene Gym - Badge reward").place_locked_item(shuffled_list[1])
            world.get_location("Castelia Gym - Badge reward").place_locked_item(shuffled_list[2])
            world.get_location("Nimbasa Gym - Badge reward").place_locked_item(shuffled_list[3])
            world.get_location("Driftveil Gym - Badge reward").place_locked_item(shuffled_list[4])
            world.get_location("Mistralton Gym - Badge reward").place_locked_item(shuffled_list[5])
            world.get_location("Icirrus Gym - Badge reward").place_locked_item(shuffled_list[6])
            world.get_location("Opelucid Gym - Badge reward").place_locked_item(shuffled_list[7])
            world.to_be_filled_locations -= 8
            for item in shuffled_list:
                items.remove(item)
        case "any_badge":
            rule: Callable[[Item], bool] = lambda item: "badge" in item.name.lower()
            world.get_location("Striaton Gym - Badge reward").item_rule = rule
            world.get_location("Nacrene Gym - Badge reward").item_rule = rule
            world.get_location("Castelia Gym - Badge reward").item_rule = rule
            world.get_location("Nimbasa Gym - Badge reward").item_rule = rule
            world.get_location("Driftveil Gym - Badge reward").item_rule = rule
            world.get_location("Mistralton Gym - Badge reward").item_rule = rule
            world.get_location("Icirrus Gym - Badge reward").item_rule = rule
            world.get_location("Opelucid Gym - Badge reward").item_rule = rule
        case "anything":
            pass
        case _:
            raise Exception(f"Bad shuffle_badges option value for player {world.player_name}")


def place_tm_hm(world: "PokemonBWWorld", items: list["PokemonBWItem"]) -> None:
    from ..data.items import tm_hm
    from ..data.locations.ingame_items.special import tm_hm_ncps, gym_tms

    match world.options.shuffle_tm_hm.current_key:
        case "shuffle":
            shuffled_list: list["PokemonBWItem"] = [
                item for item in items
                if item.name in tm_hm.tm and "TM70" not in item.name
            ]
            world.random.shuffle(shuffled_list)
            for location_name in tm_hm_ncps:
                item: "PokemonBWItem" = shuffled_list.pop()
                world.get_location(location_name).place_locked_item(item)
                items.remove(item)
                world.to_be_filled_locations -= 1
            for location_name in gym_tms:
                item: "PokemonBWItem" = shuffled_list.pop()
                world.get_location(location_name).place_locked_item(item)
                items.remove(item)
                world.to_be_filled_locations -= 1
        case "hm_with_badge":
            tms: list["PokemonBWItem"] = []
            hms: list["PokemonBWItem"] = []
            for item in items:
                if "HM0" in item.name or "TM70" in item.name:
                    hms.append(item)
                elif item.name.startswith("TM"):
                    tms.append(item)
            world.random.shuffle(tms)
            # take one random TM out and add to HMs, so that there are 8 TMs/HMs for 8 gym leaders
            hms.append(tms.pop())
            world.random.shuffle(hms)
            for location_name in gym_tms:
                item: "PokemonBWItem" = hms.pop()
                world.get_location(location_name).place_locked_item(item)
                items.remove(item)
                world.to_be_filled_locations -= 1
            for location_name in tm_hm_ncps:
                item: "PokemonBWItem" = tms.pop()
                world.get_location(location_name).place_locked_item(item)
                items.remove(item)
                world.to_be_filled_locations -= 1
        case "any_tm_hm":
            rule: Callable[[Item], bool] = lambda item: (
                (item.name.lower().startswith("tm") or item.name.lower().startswith("hm")) and item.name[2].isdigit()
            )
            for location_name in tm_hm_ncps:
                world.get_location(location_name).item_rule = rule
            for location_name in gym_tms:
                world.get_location(location_name).item_rule = rule
        case "anything":
            pass
        case _:
            raise Exception(f"Bad shuffle_tm_hm option value for player {world.player_name}")


def starting_season(world: "PokemonBWWorld", items: list["PokemonBWItem"]) -> None:
    from ..data.items import seasons

    if world.options.season_control == "randomized":
        seasons_list: list["PokemonBWItem"] = [
            item for item in items if item.name in seasons.table
        ]
        start = world.random.choice(seasons_list)
        world.push_precollected(start)
        items.remove(start)
