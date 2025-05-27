from .classification import always_progression
from .. import BadgeItemData

item_table: dict[str, BadgeItemData] = {
    "Trio Badge": BadgeItemData(0, always_progression),
    "Basic Badge": BadgeItemData(1, always_progression),
    "Insect Badge": BadgeItemData(2, always_progression),
    "Bolt Badge": BadgeItemData(3, always_progression),
    "Quake Badge": BadgeItemData(4, always_progression),
    "Jet Badge": BadgeItemData(5, always_progression),
    "Freeze Badge": BadgeItemData(6, always_progression),
    "Legend Badge": BadgeItemData(7, always_progression),
}