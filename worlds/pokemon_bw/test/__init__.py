
# Options checklist:

# goal:
#   default ghetsis
#   each other has its own test
# version:
#   always random
# randomize_wild_pokemon:
#   default []
#   one test for all modifiers
#   11 tests for "Randomize" + random selection of other modifiers
# shuffle_badges:
#   default shuffle
#   each other has its own test
# shuffle_tm_hm:
#   default shuffle
#   each other has its own test
# dexsanity:
#   default 0
#   one test for 100
#   one test for 649 + randomize_wild_pokemon = ["Randomize", "Ensure all obtainable"]
# season_control:
#   default vanilla
#   each other has its own test
# randomization_adjustments:
#   default {"Stats leniency": 10}
#   other values irrelevant
#   no other parameters so far
# modify_item_pool:
#   default []
#   one test for all modifiers combined
# modify_logic:
#   default ["Require Dowsing Machine", "Prioritize key item locations"]
#   one test for []
# reusable_tms:
#   too complex to test
