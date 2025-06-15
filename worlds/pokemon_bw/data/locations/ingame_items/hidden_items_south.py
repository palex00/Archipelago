from ... import FlagLocationData
from ..rules import *
from ..progress_type import *

# How I decided the progress types:
# I set always_default by default (pun not intended)
# If accessibility is not always given, it will be always_excluded

table: dict[str, FlagLocationData] = {
    "Route 1 - South hidden item": FlagLocationData(1023, always_default, "Route 1 West", None),
    "Route 17 - North hidden item #1": FlagLocationData(1016, always_default, "Route 17 North", None),
    "Route 17 - North hidden item #2": FlagLocationData(1017, always_default, "Route 17 North", None),
    "Route 17 - North hidden item #3": FlagLocationData(1021, always_default, "Route 17 North", None),
    "Route 17 - Central hidden item": FlagLocationData(1035, always_default, "Route 17 North", None),
    "Route 18 - Ravine hidden item": FlagLocationData(1018, always_default, "Route 18", can_use_strength),
    "Route 18 - Upper coast hidden item": FlagLocationData(1019, always_default, "Route 18 Coast", None),
    "Route 18 - Lower coast hidden item": FlagLocationData(1020, always_default, "Route 18 Coast", None),
    "Striaton City - North west hidden item #1": FlagLocationData(
        900, always_default, "Striaton City",
        lambda state, world: (can_reach_region("Route 3")(state, world) or can_use_surf(state, world))
    ),
    "Striaton City - North west hidden item #2": FlagLocationData(901, always_default, "Striaton City", can_use_surf),
    # Following region is basement because it's behind the traffic cone, which unlocks basement
    "Dreamyard - Hidden item behind traffic cone": FlagLocationData(903, always_default, "Dreamyard Basement", None),
    "Dreamyard - South hidden item in barrel": FlagLocationData(902, always_default, "Dreamyard South", None),
    "Dreamyard Basement - North east hidden item": FlagLocationData(906, always_default, "Dreamyard Basement", None),
    "Dreamyard Basement - West hidden item": FlagLocationData(1027, always_default, "Dreamyard Basement", None),
    "Dreamyard Basement - South west hidden item": FlagLocationData(907, always_default, "Dreamyard Basement", None),
    "Route 3 - Hidden item in sandbox": FlagLocationData(903, always_default, "Route 3", None),
    "Route 3 - South east or west hidden item": FlagLocationData(904, always_default, "Route 3", None),
    "Wellspring Cave - 1F hidden item #1": FlagLocationData(1062, always_default, "Wellspring Cave Entrance", None),
    "Wellspring Cave - 1F hidden item #2": FlagLocationData(1061, always_default, "Wellspring Cave Inner", None),
    "Wellspring Cave - B1F south hidden item": FlagLocationData(1064, always_default, "Wellspring Cave Inner", None),
    "Wellspring Cave - B1F hidden item south east of trainers": FlagLocationData(1063, always_default, "Wellspring Cave Inner", None),
    "Wellspring Cave - B1F hidden item north west of trainers": FlagLocationData(1036, always_default, "Wellspring Cave Inner", None),
    "Wellspring Cave - B1F north hidden item": FlagLocationData(1022, always_default, "Wellspring Cave Inner", None),
    "Nacrene City - Hidden item on railway": FlagLocationData(905, always_default, "Nacrene City", None),
    "Nacrene City - Hidden item near Café Warehouse": FlagLocationData(940, always_default, "Nacrene City", None),
    "Pinwheel Forest - Outside north hidden item": FlagLocationData(941, always_default, "Pinwheel Forest Outside", None),
    "Pinwheel Forest - Outside south east hidden item": FlagLocationData(908, always_default, "Pinwheel Forest Outside", None),
    "Pinwheel Forest - Outside south hidden item": FlagLocationData(942, always_default, "Pinwheel Forest Outside", None),
    "Pinwheel Forest - Outside hidden item behind dark grass": FlagLocationData(943, always_default, "Pinwheel Forest Outside", None),
    "Pinwheel Forest - West hidden item inside tree stump": FlagLocationData(945, always_default, "Pinwheel Forest West", None),
    "Pinwheel Forest - South west hidden item": FlagLocationData(1075, always_default, "Pinwheel Forest West", None),
    "Pinwheel Forest - East hidden item": FlagLocationData(944, always_default, "Pinwheel Forest East", None),
    "Liberty Garden - Hidden item in trash can": FlagLocationData(1042, always_default, "Liberty Garden", None),
    "Route 4 - South west hidden item": FlagLocationData(1059, always_default, "Route 4 South", None),
    "Route 4 - Central hidden item": FlagLocationData(946, always_default, "Route 4 South", None),
    "Route 4 - Hidden item near buildings #1": FlagLocationData(1058, always_default, "Route 4 South", None),
    "Route 4 - Hidden item near buildings #2": FlagLocationData(1076, always_default, "Route 4 South", None),
    "Route 4 - North east hidden item": FlagLocationData(947, always_default, "Route 4 North", None),
    "Desert Resort - South hidden item": FlagLocationData(1029, always_default, "Desert Resort", None),
    "Desert Resort - West hidden item": FlagLocationData(949, always_default, "Desert Resort", None),
    "Desert Resort - North east hidden item": FlagLocationData(950, always_default, "Desert Resort", None),
    "Desert Resort - Hidden item near tower": FlagLocationData(948, always_default, "Desert Resort", None),
    "Relic Castle - B1F castleside hidden item": FlagLocationData(1051, always_default, "Relic Castle Entrance", None),
    "Relic Castle - B4F castleside hidden item": FlagLocationData(1052, always_default, "Relic Castle Lower Floors", None),
    "Relic Castle - B3F towerside hidden item": FlagLocationData(951, always_default, "Relic Castle Tower Lower Floors", None),
    "Nimbasa City - Hidden item near ferris wheel": FlagLocationData(952, always_default, "Nimbasa City", None),
    "Anville Town - North hidden item": FlagLocationData(1041, always_default, "Anville Town", None),
}
