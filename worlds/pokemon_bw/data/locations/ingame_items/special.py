from ..rules import *
from ..progress_type import *
from ..checking_type import *
from ... import FlagLocationData

gym_badges: dict[str, FlagLocationData] = {
    "Striaton Gym - Badge reward": FlagLocationData(0x172, always_priority, "Striaton City", None),
    "Nacrene Gym - Badge reward": FlagLocationData(0x173, always_priority, "Nacrene City", None),
    "Castelia Gym - Badge reward": FlagLocationData(0x174, always_priority, "Castelia City", None),
    "Nimbasa Gym - Badge reward": FlagLocationData(0x175, always_priority, "Nimbasa City", None),
    "Driftveil Gym - Badge reward": FlagLocationData(0x176, always_priority, "Driftveil City", None),
    "Mistralton Gym - Badge Reward": FlagLocationData(0x177, always_priority, "Mistralton City", None),
    "Icirrus Gym - Badge Reward": FlagLocationData(0x178, always_priority, "Icirrus City", None),
    "Opelucid Gym - Badge reward": FlagLocationData(0x179, always_priority, "Opelucid City", None),
}

tm_hm_ncps: dict[str, FlagLocationData] = {
    "Nuvema Town - TM from Professor Juniper for seeing 25 species": FlagLocationData(174, always_default, "Nuvema Town", has_number_of_species(25)),  #
    "Nuvema Town - TM from Professor Juniper for seeing 60 species": FlagLocationData(175, always_default, "Nuvema Town", has_number_of_species(60)),  #
    "Nuvema Town - TM from Professor Juniper for seeing 115 species": FlagLocationData(176, always_default, "Nuvema Town", has_number_of_species(115)),  #
    "Route 18 - TM from sage Rood": FlagLocationData(0x186, always_default, "Route 18", can_reach_region("Pokémon League")),  #
    "Striaton City - TM from Fennel": FlagLocationData(0x18D, always_default, "Striaton City", None),  #
    "Striaton Gym - TM reward": FlagLocationData(0x172, always_default, "Striaton City", None),  #
    "Dreamyard - TM from sage Gorm": FlagLocationData(0x19A, always_default, "Dreamyard South", None),  #
    "Nacrene Gym - TM reward": FlagLocationData(0x173, always_default, "Nacrene City", None),  #
    "Pinwheel Forest Outside - TM from woman near Nacrene City": FlagLocationData(271, always_default, "Pinwheel Forest Outside", None),  #
    "Castelia City - TM from hiker in building in Castelia Street": FlagLocationData(265, always_default, "Castelia City", None),  #
    "Castelia City - TM from man in black behind dumpster": FlagLocationData(0x197, always_default, "Castelia City", None),  #
    "Castelia City - TM from school kid in building in northern street": FlagLocationData(270, always_default, "Castelia City", None),  #
    "Castelia City - TM from Mr. Lock in building in northern street": FlagLocationData(308, always_default, "Castelia City", has_item("Lock Capsule")),  #
    "Castelia Gym - TM reward": FlagLocationData(0x174, always_default, "Castelia City", None),  #
    "Route 4 - TM from worker in northern building": LocationData(0000000, always_default, "Route 4 North", None),  # TODO
    "Relic Castle - TM from sage Ryoku": LocationData(0000000, always_default, "Relic Castle Basement", None),  # TODO
    "Nimbasa City - TM from ace trainer in western building": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Nimbasa Gym - TM reward": FlagLocationData(0x175, always_default, "Nimbasa City", None),  #TODO
    "Nimbasa City - TM from lady in Musical Theater": LocationData(0000000, always_default, "Nimbasa City", None),  # TODO
    "Driftveil City - TM from Bianca": LocationData(0000000, always_default, "Driftveil City", None),  # TODO
    "Cold Storage Building - TM from sage Zinzolin": LocationData(0000000, always_default, "Cold Storage", can_reach_region("Pokémon League")),  # TODO
    "Route 6 - TM from Clay": LocationData(0000000, always_default, "Route 6", None),  # TODO
    "Chargestone Cave - TM from sage Bronius": LocationData(0000000, always_default, "Chargestone Cave", can_reach_region("Pokémon League")),  # TODO
    "Mistralton Gym - TM reward": FlagLocationData(0x177, always_default, "Mistralton City", None),  #TODO
    "Route 7 - TM from battle girl": LocationData(0000000, always_default, "Route 7", None),  # TODO
    # The map this item is placed on belongs to Twist Mountain, but it's always accessible from route 7
    "Twist Mountain - TM from Alder": LocationData(0000000, always_default, "Route 7", None),  # TODO
    "Icirrus City - TM from old lady in pokémon center": LocationData(0000000, always_default, "Icirrus City", None),  # TODO
    "Icirrus Gym - TM reward": FlagLocationData(0x178, always_default, "Icirrus City", None),  #TODO
    "Route 8 - TM from western parasol lady": LocationData(0000000, always_default, "Route 8", None),  # TODO
    "Tubeline Bridge - TM from battle girl": LocationData(0000000, always_default, "Tubeline Bridge", None),  # TODO
    "Route 9 - TM from infielder": LocationData(0000000, always_default, "Route 9", None),  # TODO
    "Route 14 - TM from sage Giallo": LocationData(0000000, always_default, "Route 14", can_use_waterfall),  # TODO
    "Undella Town - TM from girl": LocationData(0000000, always_default, "Undella Town", None),  # TODO
    "Route 13 - TM from Wingull": LocationData(0000000, always_default, "Route 13", has_all_items("Wingull Gram 1", "Wingull Gram 2", "Wingull Gram 3")),  # TODO
    "Opelucid Gym - TM reward": FlagLocationData(0x179, always_default, "Opelucid City", None),  #TODO
}
