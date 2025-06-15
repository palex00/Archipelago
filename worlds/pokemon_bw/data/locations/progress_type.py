from BaseClasses import LocationProgressType
from .. import ProgressTypeMethod


always_priority: ProgressTypeMethod = lambda options, world: LocationProgressType.PRIORITY

always_default: ProgressTypeMethod = lambda options, world: LocationProgressType.DEFAULT

always_excluded: ProgressTypeMethod = lambda options, world: LocationProgressType.EXCLUDED
