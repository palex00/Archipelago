from ..rules import *
from ..progress_type import *
from ... import FlagLocationData

gym_badges: dict[str, FlagLocationData] = {
    "Striaton Gym - Badge reward": FlagLocationData(0x172, always_priority, "Striaton City", None, None),
    "Nacrene Gym - Badge reward": FlagLocationData(0x173, always_priority, "Nacrene City", None, None),
    "Castelia Gym - Badge reward": FlagLocationData(0x174, always_priority, "Castelia City", None, None),
    "Nimbasa Gym - Badge reward": FlagLocationData(0x175, always_priority, "Nimbasa City", None, None),
    "Driftveil Gym - Badge reward": FlagLocationData(0x176, always_priority, "Driftveil City", None, None),
    "Mistralton Gym - Badge reward": FlagLocationData(0x177, always_priority, "Mistralton City", None, None),
    "Icirrus Gym - Badge reward": FlagLocationData(0x178, always_priority, "Icirrus City", None, None),
    "Opelucid Gym - Badge reward": FlagLocationData(0x179, always_priority, "Opelucid City", None, None),
}

gym_tms: dict[str, FlagLocationData] = {
    "Striaton Gym - TM reward": FlagLocationData(0x172, always_default, "Striaton City", None, None),
    "Nacrene Gym - TM reward": FlagLocationData(0x173, always_default, "Nacrene City", None, None),
    "Castelia Gym - TM reward": FlagLocationData(0x174, always_default, "Castelia City", None, None),
    "Nimbasa Gym - TM reward": FlagLocationData(0x175, always_default, "Nimbasa City", None, None),
    "Route 6 - TM from Clay": FlagLocationData(0x1A2, always_default, "Route 6", None, has_quake_badge),
    "Mistralton Gym - TM reward": FlagLocationData(0x177, always_default, "Mistralton City", None, None),
    "Icirrus Gym - TM reward": FlagLocationData(0x178, always_default, "Icirrus City", None, None),
    "Opelucid Gym - TM reward": FlagLocationData(0x179, always_default, "Opelucid City", None, None),
}

tm_hm_ncps: dict[str, FlagLocationData] = {
    "Nuvema Town - TM from Professor Juniper for seeing 25 species": FlagLocationData(174, always_default, "Nuvema Town", None, has_25_species),
    "Nuvema Town - TM from Professor Juniper for seeing 60 species": FlagLocationData(175, always_default, "Nuvema Town", None, has_60_species),
    "Nuvema Town - TM from Professor Juniper for seeing 115 species": FlagLocationData(176, always_default, "Nuvema Town", None, has_115_species),
    "Route 18 - TM from sage Rood": FlagLocationData(0x186, always_default, "Route 18", None, can_beat_ghetsis),
    "Striaton City - TM from Fennel": FlagLocationData(0x18D, always_default, "Striaton City", None, None),
    "Dreamyard - TM from sage Gorm": FlagLocationData(0x19A, always_default, "Dreamyard South", None, None),
    "Pinwheel Forest Outside - TM from woman near Nacrene City": FlagLocationData(271, always_default, "Pinwheel Forest Outside", None, None),
    "Castelia City - TM from hiker in building in Castelia Street": FlagLocationData(265, always_default, "Castelia City", None, None),
    "Castelia City - TM from man in black behind dumpster": FlagLocationData(0x197, always_default, "Castelia City", None, None),
    "Castelia City - TM from school kid in building in northern street": FlagLocationData(270, always_default, "Castelia City", None, None),
    "Castelia City - TM from Mr. Lock in building in northern street": FlagLocationData(308, always_default, "Castelia City", None, has_lock_capsule),
    "Route 4 - TM from worker in northern building": FlagLocationData(272, always_default, "Route 4 North", None, None),
    "Relic Castle - TM from sage Ryoku": FlagLocationData(0x19D, always_default, "Relic Castle Basement", None, None),
    "Nimbasa City - TM from ace trainer in western building": FlagLocationData(290, always_default, "Nimbasa City", None, None),
    "Nimbasa City - TM from lady in Musical Theater": FlagLocationData(267, always_default, "Nimbasa City", None, None),
    "Driftveil City - TM from Bianca": FlagLocationData(0x1A0, always_default, "Driftveil City", None, None),
    "Cold Storage - TM from sage Zinzolin": FlagLocationData(0x1A1, always_default, "Cold Storage", None, can_beat_ghetsis),
    "Chargestone Cave - TM from sage Bronius": FlagLocationData(0x1A4, always_default, "Chargestone Cave", None, can_beat_ghetsis),
    "Route 7 - TM from battle girl": FlagLocationData(133, always_default, "Route 7", None, None),
    # The map this item is placed on belongs to Twist Mountain, but it's always accessible from route 7
    "Twist Mountain - TM from Alder": FlagLocationData(0x1A5, always_default, "Route 7", None, None),
    "Icirrus City - TM from old lady in pokémon center": FlagLocationData(135, always_default, "Icirrus City", None, None),
    "Route 8 - TM from western parasol lady": FlagLocationData(258, always_default, "Route 8", None, None),
    "Tubeline Bridge - TM from battle girl": FlagLocationData(260, always_default, "Tubeline Bridge", None, None),
    "Route 9 - TM from infielder": FlagLocationData(0x1A9, always_default, "Route 9", None, None),
    "Route 14 - TM from sage Giallo": FlagLocationData(0x1AD, always_default, "Route 14", None, can_use_waterfall),
    "Undella Town - TM from girl": FlagLocationData(346, always_default, "Undella Town", None, None),
    "Route 13 - TM from Wingull": FlagLocationData(0x1AE, always_default, "Route 13", None, has_all_grams),
}
