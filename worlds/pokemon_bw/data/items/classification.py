from BaseClasses import ItemClassification
from .. import ClassificationMethod


always_progression: ClassificationMethod = lambda options, world: ItemClassification.progression

always_useful: ClassificationMethod = lambda options, world: ItemClassification.useful

always_filler: ClassificationMethod = lambda options, world: ItemClassification.filler

always_trap: ClassificationMethod = lambda options, world: ItemClassification.trap

tm_hm_hunt: ClassificationMethod = lambda options, world: (
    ItemClassification.progression
    if options.goal == "tmhm_hunt" else ItemClassification.useful
)
