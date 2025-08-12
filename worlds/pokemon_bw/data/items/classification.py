from BaseClasses import ItemClassification
from .. import ClassificationMethod


always_progression: ClassificationMethod = lambda world: ItemClassification.progression

always_useful: ClassificationMethod = lambda world: ItemClassification.useful

always_filler: ClassificationMethod = lambda world: ItemClassification.filler

always_trap: ClassificationMethod = lambda world: ItemClassification.trap

tm_hm_hunt: ClassificationMethod = lambda world: (
    ItemClassification.progression_skip_balancing
    if world.options.goal == "tmhm_hunt" else ItemClassification.useful
)
