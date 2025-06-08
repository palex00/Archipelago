# Changelog
Versions are sorted in ascending order, i.e. the most recent changes are at the top.

## 0.1.0: First release

### Rom
- Removed most ItemAdd commands (to only get items sent from the client)
- Removed some ItemSub commands (to not loose key items)
- Changed most HasBadge and AddBadge commands to checking for and setting a custom flag
  - Those flags are all within global var 0x4137, which is set to 0 when opening the starter gift box
- Set the unusable/untrashable flag for unused key items
- Changed some roadblocks
  - Man hindering the player from entering route 3 now requires the parcel
  - Traffic cone in Dreamyard blocking the basement now vanishes when talking to it with the basement key
  - The grunts blocking the entrance to Pinwheel Forest now look for the loot sack
  - A shadow triad member now blocks you from leaving Pinwheel Forest without the dragon skull
  - The worker in the middle of route 4 is now looking for the machine part
  - The worker blocking you from going to B2F and below in Relic Castle now requires the explorer kit
  - The workers blocking Marvelous Bridge now let you pass with a blue card
    - They were also moved a little bit to prevent one-way passing from the other side
  - Entering Driftveil Drawbridge now requires a tidal bell, even coming from Driftveil City
  - The spider web blocking Chargestone Cave was multiplied and moved a bit south to prevent one-way passing
    - The script was also slightly altered to check for the quake badge instead of a flag
  - The worker blocking Twist Mountain was moved a bit to prevent one-way passing
    - The script was also slightly altered to check for the jet badge instead of a flag
  - The grunts blocking Tubeline Bridge now disappear when seeing the light or dark stone
    - They were also moved a little bit to prevent one-way passing from
  - The black belt blocking Challenger's Cave now vanishes when receiving the red chain
  - The police officer blocking the gate between Opelucid City and route 11 now requires Oak's letter to pass

### APWorld

- Roadmap
- Credits
- Item data: Bag items and badges
- Location data: Dexsanity
- Encounter data: Viable dexsanity, regions, slots
- Species data

### Client
