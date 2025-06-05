from . import classification
from .. import BadgeItemData

item_table: dict[str, BadgeItemData] = {
    "Trio Badge": BadgeItemData(0, classification.always_progression),
    "Basic Badge": BadgeItemData(1, classification.always_progression),
    "Insect Badge": BadgeItemData(2, classification.always_progression),
    "Bolt Badge": BadgeItemData(3, classification.always_progression),
    "Quake Badge": BadgeItemData(4, classification.always_progression),
    "Jet Badge": BadgeItemData(5, classification.always_progression),
    "Freeze Badge": BadgeItemData(6, classification.always_progression),
    "Legend Badge": BadgeItemData(7, classification.always_progression),
}
