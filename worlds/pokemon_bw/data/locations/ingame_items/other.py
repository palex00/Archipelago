from ..checking_type import *
from ..rules import *
from ..progress_type import *
from ... import FlagLocationData

# How I decided the progress types:
# I set always_default by default (pun not intended)
# If the npc/... gives you a progression key item, it will be always_priority
# If accessibility is not always given, it will be always_excluded

table: dict[str, FlagLocationData] = {
    "Nuvema Town - Item #1 from Mom": FlagLocationData(0x189, always_default, "Nuvema Town", None),
    "Nuvema Town - Item #2 from Mom": FlagLocationData(0x185, always_default, "Nuvema Town", None),
    "Nuvema Town - Item from Looker": FlagLocationData(0x18A, always_priority, "Nuvema Town", can_reach_region("Pokémon League")),
    "Route 1 - Item after catching tutorial #1": FlagLocationData(0x18B, always_default, "Route 1 East", None),  #
    "Route 1 - Item after catching tutorial #2": FlagLocationData(0x18B, always_default, "Route 1 East", None),  #
    "Route 1 - Item after catching tutorial #3": FlagLocationData(0x18B, always_default, "Route 1 East", None),  #
    "Route 1 - Item after catching tutorial #4": FlagLocationData(0x18B, always_default, "Route 1 East", None),  #
    "Route 1 - Item after catching tutorial #5": FlagLocationData(0x18B, always_default, "Route 1 East", None),  #
    "Route 1 - Item from woman": FlagLocationData(132, always_default, "Route 1 East", None),  #
    "Route 1 - Item from ranger Brenda": FlagLocationData(1420+531, always_default, "Route 1 West", None),  #
    "Route 1 - Item from ranger Claude": FlagLocationData(1420+532, always_default, "Route 1 West", None),  #
    # Requires pokémon being randomized
    # "P2 Laboratory - Item #1 from scientist": LocationData(0000000, always_default, "P2 Laboratory", has_species("Genesect")),  #
    # "P2 Laboratory - Item #2 from scientist": LocationData(0000000, always_default, "P2 Laboratory", has_species("Genesect")),  #
    "Accumula Town - Item from man in north west building": FlagLocationData(109, always_default, "Accumula Town", None),  #
    "Striaton City - Item from man in south east building": FlagLocationData(111, always_default, "Striaton City", None),  #
    "Striaton City - Item from roughneck": FlagLocationData(189, always_default, "Striaton City", None),  #
    "Striaton City - Item from Cheren #1": FlagLocationData(192, always_default, "Striaton City", None),  #
    "Striaton City - Item from Cheren #2": FlagLocationData(192, always_default, "Striaton City", None),  #
    "Striaton City - Item from Cheren #3": FlagLocationData(192, always_default, "Striaton City", None),  #
    "Striaton City - Item from boy in Trainer's School": FlagLocationData(190, always_default, "Striaton City", None),  #
    "Striaton City - Item from Amanita": FlagLocationData(0x18C, always_default, "Striaton City", can_reach_region("Dreamyard North")),  #
    "Striaton City - Item from fisherman": FlagLocationData(187, always_default, "Striaton City", can_use_surf),  #
    "Striaton Gym - Gym guide item": FlagLocationData(118, always_default, "Striaton City", None),  #
    "Route 3 - Item from pokémon breeder Adelaide": FlagLocationData(1420+20, always_default, "Route 3", None),  #
    "Route 3 - Item from girl after Wellspring Cave #1": FlagLocationData(0x18E, always_default, "Route 3", None),  #
    "Route 3 - Item from girl after Wellspring Cave #2": FlagLocationData(0x18E, always_default, "Route 3", None),  #
    "Route 3 - Item from girl after Wellspring Cave #3": FlagLocationData(0x18E, always_default, "Route 3", None),  #
    "Route 3 - Item from pokémon breeder Galen": FlagLocationData(1420+19, always_default, "Route 3", can_use_surf),  #
    "Nacrene City - Item from Cheren #1": FlagLocationData(0x194, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from Cheren #2": FlagLocationData(0x194, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from Cheren #3": FlagLocationData(0x194, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from girl in west building": FlagLocationData(301, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from waitress in Café Warehouse": FlagLocationData(2736, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from Bianca": FlagLocationData(0x18F, always_default, "Nacrene City", None),  #
    "Nacrene City - Item from Lenora": FlagLocationData(0x195, always_priority, "Nacrene City", can_reach_region("Relic Castle Lower Floors")),  #
    "Nacrene Gym - Gym guide item": FlagLocationData(119, always_default, "Nacrene City", None),  #
    "Pinwheel Forest Outside - Item from challenge rock": FlagLocationData(2737, always_default, "Pinwheel Forest Outside", has_fighting_type_species),  #
    "Pinwheel Forest - Item from ranger Forrest": FlagLocationData(1420+26, always_default, "Pinwheel Forest West", None),  #
    "Pinwheel Forest - Item from ranger Audra": FlagLocationData(1420+29, always_default, "Pinwheel Forest West", None),  #
    "Pinwheel Forest - Item from ranger Irene": FlagLocationData(1420+27, always_default, "Pinwheel Forest West", None),  #
    "Pinwheel Forest - Item from ranger Miguel": FlagLocationData(1420+28, always_default, "Pinwheel Forest West", None),  #
    "Pinwheel Forest - Stolen item from Plasma grunt": FlagLocationData(0x187, always_priority, "Pinwheel Forest West", None),  #
    "Pinwheel Forest - Item from Lenora": FlagLocationData(0x188, always_default, "Pinwheel Forest West", None),  #
    "Skyarrow Bridge - Item from hiker in gate": FlagLocationData(268, always_default, "Skyarrow Bridge", None),  #
    "Castelia City - Item from scientist at Thumb Pier": FlagLocationData(269, always_default, "Castelia City", None),  # 
    # The following locations involve trading and I don't know yet how to handle them
    # Not changing the script
    # "Castelia City Pokémon Center - Item by man in black for 5 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    # "Castelia City Pokémon Center - Item by man in black for 10 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    # "Castelia City Pokémon Center - Item by man in black for 20 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    # "Castelia City Pokémon Center - Item by man in black for 30 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    # "Castelia City Pokémon Center - Item by man in black for 40 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    # "Castelia City Pokémon Center - Item by man in black for 50 different IDs": LocationData(0000000, always_excluded, "Castelia City", AAAAAA),  #
    "Battle Company - 47F item from clerk #1": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from clerk #2": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from clerk #3": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from clerk #4": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from clerk #5": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from clerk #6": FlagLocationData(266, always_default, "Castelia City", None),  #
    "Battle Company - 47F item from scientist": FlagLocationData(191, always_default, "Castelia City", None),  #
    "Battle Company - 55F item from President Geoff": FlagLocationData(163, always_default, "Castelia City", None),  #
    "Castelia City - Item from harlequin in Studio Castelia": FlagLocationData(2733, always_default, "Castelia City", None),  #
    "Castelia City - Item from manager in Café Sonata": FlagLocationData(164, always_default, "Castelia City", None),  #
    "Castelia City - Item from Iris in Plasma hideout": FlagLocationData(0x199, always_default, "Castelia City", None),  #
    "Castelia City - Item from dancers": FlagLocationData(0x196, always_default, "Castelia City", None),  #
    "Castelia City - Item from scientist in building in northern street": FlagLocationData(328, always_default, "Castelia City", has_number_of_species(25)),  #
    # The rom editor cannot decompile the script for the Passerby Analytics HQ properly
    # "Passerby Analytics HQ - Item for answering all questionnaires": LocationData(0000000, always_default, "Castelia City", None),  #
    # I think this one requires connecting with other save files too
    # Not changing the script
    # "Passerby Analytics HQ - Item for completing all survey requests": LocationData(0000000, always_default, "Castelia City", None),  #
    "Castelia Gym - Gym guide item": FlagLocationData(120, always_default, "Castelia City", None),  #
    "Royal Unova - Item for defeating every trainer": FlagLocationData(0x198, always_default, "Castelia City", can_reach_region("Pokémon League")),  #
    "Route 4 - Item from Professor Juniper #1": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #2": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #3": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #4": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #5": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #6": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #7": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #8": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #9": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Route 4 - Item from Professor Juniper #10": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Desert Resort - Item from man in black": LocationData(0000000, always_default, "Desert Resort", None),  # TODO
    "Desert Resort - Item from ranger Mylene": LocationData(0000000, always_default, "Desert Resort", None),  # TODO
    "Desert Resort - Item from ranger Jaden": LocationData(0000000, always_default, "Desert Resort", None),  # TODO
    "Desert Resort - Item from Professor Juniper": LocationData(0000000, always_default, "Desert Resort", can_reach_region("Pokémon League")),  # TODO
    "Relic Castle - 1F castleside item from backpacker": LocationData(0000000, always_default, "Relic Castle Entrance", None),  # TODO
    "Nimbasa City - Item from Day-Care man": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from socialite in western building": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from ace trainer exiting battle subway": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from ace trainer in another western building": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from man in eastern gate": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa Gym - Gym guide item": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    # Following trainers are said to appear randomly each day in big stadium or small court
    "Nimbasa City - Item from waiter Clint": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from waitress Bonita": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from nurse Kirsten": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from doctor Jules": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from baker Lilly": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from scientist Simon": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from scientist Blythe": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from ace trainer Lucille": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from ace trainer Charlie": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from veteran Arlen": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from veteran Sayuri": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from nursery Aide Leah": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from youngster Kevin": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from lass Dana": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from backpacker Alexander": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from backpacker Patty": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from socialite Emilia": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from gentleman Renaud": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    # Following items require such an amount of effort that having important items here might be a problem
    "Battle Subway - Item from janitor on non-super platforms for 21 consecutive wins": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Battle Subway - Item from artist on super platforms for 21 consecutive wins": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Battle Subway - Item from ace trainer on super platforms for 28 consecutive wins": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Battle Subway - Item from clerk on super platforms for 105 consecutive wins": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Battle Subway - Item from ace trainer on super platforms for 203 consecutive wins": LocationData(0000000, always_excluded, "Nimbasa City", None),  # TODO
    "Nimbasa City - Item from Musical Theater owner": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Anville Town - Item from depot agent on first visit": LocationData(0000000, always_default, "Anville Town", None),  # TODO
    "Driftveil City - Item from man for seeing more than 50 pokémon": LocationData(0000000, always_default, "Driftveil City", has_number_of_species(51)),  # TODO
    "Driftveil City - Item from girl in pokémon center #1": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    "Driftveil City - Item from girl in pokémon center #2": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    "Driftveil City - Item from girl in pokémon center #3": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    "Driftveil City - Item from man in black in market": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    # That lady is asking for a random TM move every day
    "Driftveil City - Item from lady asking for a pokémon knowing a certain TM move": LocationData(0000000, always_excluded, "Driftveil City", None),  # TODO
    "Driftveil Gym - Gym guide item": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    "Cold Storage - Item from worker": LocationData(0000000, always_default, "Cold Storage", None),  # TODO
    "Route 6 - Item from ranger Shanti": LocationData(0000000, always_default, "Route 6", None),  # TODO
    "Route 6 - Item from ranger Richard": LocationData(0000000, always_default, "Route 6", None),  # TODO
    "Route 6 - Item from scientist for all Deerling forms": LocationData(0000000, season_dependant, "Route 6", can_catch_all_deerlings),  # TODO
    "Route 6 - Item from child in western house": LocationData(0000000, always_default, "Route 6", None),  # TODO
    "Chargestone Cave - Item from Professor Juniper": LocationData(0000000, always_default, "Chargestone Cave", None),  # TODO
    "Chargestone Cave - Item from nugget brothers #1": LocationData(0000000, always_default, "Chargestone Cave", None),  # TODO
    "Chargestone Cave - Item from nugget brothers #2": LocationData(0000000, always_default, "Chargestone Cave", None),  # TODO
    "Mistralton City - Item from veteran in Cargo Service building": LocationData(0000000, always_default, "Mistralton City", None),  # TODO
    "Mistralton Gym - Gym guide item": LocationData(0000000, always_excluded, "Mistralton City", None),  # TODO
    "Route 7 - Item from ranger Mary": LocationData(0000000, always_default, "Route 7", None),  # TODO
    "Route 7 - Item from ranger Pedro": LocationData(0000000, always_default, "Route 7", None),  # TODO
    "Twist Mountain - Item from worker near ice rock cave": LocationData(0000000, always_default, "Twist Mountain", can_reach_region("Pokémon League")),  # TODO
    "Icirrus City - Item from Aha if answer was correct": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    "Icirrus City - Item from Aha if answer was incorrect": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    "Icirrus City - Item from Pokémon Fan Club chairman for gaining 25 levels": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    "Icirrus City - Item from Pokémon Fan Club chairman for gaining 50 levels": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    # This is not only unreasonable, but also has an astronomically low softlock chance if we don't document breeding data and consider it during generation
    "Icirrus City - Item from Pokémon Fan Club chairman for gaining 99 levels": LocationData(0000000, always_excluded, "Icirrus City", None),  # TODO
    "Icirrus City - Item from the former Team Rocket member's wife": LocationData(0000000, season_dependant, "Icirrus City", can_set_winter),  # TODO
    "Icirrus Gym - Gym guide item": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    "Dragonspiral Tower - Item from Cedric Juniper": LocationData(0000000, always_default, "Dragonspiral Tower", None),  # TODO
    "Route 8 - Item from Bianca": LocationData(0000000, always_default, "Route 8", can_reach_region("Relic Castle Lower Floors")),  # TODO
    "Route 8 - Item from ranger Lewis": LocationData(0000000, always_default, "Route 8", None),  # TODO
    "Route 8 - Item from ranger Annie": LocationData(0000000, always_default, "Route 8", None),  # TODO
    "Route 8 - Item from eastern parasol lady": LocationData(0000000, always_default, "Route 8", None),  # TODO
    "Moor of Icirrus - Item from ranger Chloris": LocationData(0000000, always_default, "Moor of Icirrus", None),  # TODO
    "Moor of Icirrus - Item from ranger Harry": LocationData(0000000, always_default, "Moor of Icirrus", None),  # TODO
    "Shopping Mall Nine - Item from worker": LocationData(0000000, always_default, "Route 9", None),  # TODO
    "Marvelous Bridge - Item from Shadow Triad #1": LocationData(0000000, always_default, "Marvelous Bridge", None),  # TODO
    "Marvelous Bridge - Item from Shadow Triad #2": LocationData(0000000, always_default, "Marvelous Bridge", None),  # TODO
    "Marvelous Bridge - Item from Shadow Triad #3": LocationData(0000000, always_default, "Marvelous Bridge", None),  # TODO
    "Marvelous Bridge - Patrat shuffle reward": LocationData(0000000, always_default, "Marvelous Bridge", None),  # TODO
    "Route 15 - Item from ranger Shelly": LocationData(0000000, always_default, "Route 15", None),  # TODO
    "Route 15 - Item from ranger Keith": LocationData(0000000, always_default, "Route 15", None),  # TODO
    "Undella Town - Item from man in Pokémon Center": LocationData(0000000, always_default, "Undella Town", None),  # TODO
    "Route 13 - Item from veteran in western house #1": LocationData(0000000, always_default, "Route 13", can_use_surf),  # TODO
    "Route 13 - Item from veteran in western house #2": LocationData(0000000, always_default, "Route 13", can_use_surf),  # TODO
    # The following 2 locations normally have wingull grams, which are progressive key items
    "Route 13 - Item from old man": LocationData(0000000, always_priority, "Route 13", None),  # TODO
    "Route 13 - Item from parasol lady": LocationData(0000000, always_priority, "Route 13", None),  # TODO
    "Lacunosa Town - Item from executive": LocationData(0000000, always_default, "Lacunosa Town", None),  # TODO
    # Requires pokémon being randomized
    # "Lacunosa Town - Item from girl for showing a Shaymin": LocationData(0000000, always_default, "Lacunosa Town", has_species("Shaymin")),  # TODO
    "Route 12 - Item from breeder Ethel #1": LocationData(0000000, always_default, "Route 12", None),  # TODO
    "Route 12 - Item from breeder Ethel #2": LocationData(0000000, always_default, "Route 12", None),  # TODO
    "Village Bridge - Item from baker Chris": LocationData(0000000, always_default, "Village Bridge", None),  # TODO
    # Following 5 items require a random pokémon every day
    "Village Bridge - Item from fisherman for showing a certain pokémon #1": LocationData(0000000, always_excluded, "Village Bridge", None),  # TODO
    "Village Bridge - Item from fisherman for showing a certain pokémon #2": LocationData(0000000, always_excluded, "Village Bridge", None),  # TODO
    "Village Bridge - Item from fisherman for showing a certain pokémon #3": LocationData(0000000, always_excluded, "Village Bridge", None),  # TODO
    "Village Bridge - Item from fisherman for showing a certain pokémon #4": LocationData(0000000, always_excluded, "Village Bridge", None),  # TODO
    "Village Bridge - Item from fisherman for showing a certain pokémon #5": LocationData(0000000, always_excluded, "Village Bridge", None),  # TODO
    "Route 11 - Item from ranger Thalia": LocationData(0000000, always_default, "Route 11", None),  # TODO
    "Route 11 - Item from ranger Crofton": LocationData(0000000, always_default, "Route 11", can_use_waterfall),  # TODO
    "Opelucid City - Item from female NPC in northern house": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    "Opelucid City - Item from linebacker in Drayden's house": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    "Opelucid City - Item from female NPC in Drayden's house": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    "Opelucid Gym - Gym guide item": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    # Don't know how to handle pokémon from other version
    # Not changing the script
    # "Opelucid City - Item from NPC for showing a pokémon knowing Charge from opposite version": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    "Opelucid City - Item from Professor Juniper": LocationData(0000000, always_default, "Opelucid City", None),  # TODO
    "Route 10 - Item from veteran near northern bridge": LocationData(0000000, always_default, "Route 10", None),  # TODO
    "Route 10 - Item from Bianka #1": LocationData(0000000, always_default, "Route 10", None),  # TODO
    "Route 10 - Item from Bianka #2": LocationData(0000000, always_default, "Route 10", None),  # TODO
    "N's Castle - Item from grunt in 3F left room": LocationData(0000000, always_default, "N's Castle", None),  # TODO
}
