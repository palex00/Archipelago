# Changelog
Versions are sorted in ascending order, i.e. the most recent changes are at the top.

## 0.1.0: First release

### Rom

#### Gameplay
- Changed some roadblocks
  - Man hindering the player from entering route 3 now requires the parcel
  - Traffic cone in Dreamyard blocking the basement now vanishes when coming close to it with the basement key
  - The grunts blocking the entrance to Pinwheel Forest now look for the loot sack
  - A shadow triad member now blocks you from leaving Pinwheel Forest without the dragon skull
  - The worker in the middle of route 4 is now looking for the machine part
  - The worker blocking you from going to B2F and below in Relic Castle now requires the explorer kit
  - The workers blocking Marvelous Bridge now let you pass with a blue card
    - They were also moved a little bit to prevent one-way passing from the other side
  - Entering Driftveil Drawbridge now requires a tidal bell, even coming from Driftveil City
  - The spider web blocking Chargestone Cave was multiplied and moved a bit south to prevent one-way passing
    - The script was also slightly altered to check for the quake badge instead of having Clay defeated
  - The worker blocking Twist Mountain was moved a bit to prevent one-way passing
    - The script was also slightly altered to check for the jet badge instead of having Skyla defeated
  - The grunts blocking Tubeline Bridge now disappear when seeing the light or dark stone
    - They were also moved a little bit to prevent one-way passing from the other side
  - The black belt blocking Challenger's Cave now vanishes when receiving the red chain
  - The police officer blocking the gate between Opelucid City and route 11 now requires Oak's letter to pass
- Made evolution items available to purchase or receive multiple times
  - Fire, water, and leaf stone in Castelia City
  - Thunder stone and metal coat in Chargestone Cave
  - Moon and sun stone in Twist Mountain
  - Dusk, dawn, and shiny stone on route 10
  - King's rock, protector, dragon scale, reaper cloth, and oval stone in Shopping Mall Nine
  - Electirizer, magmarizer, upgrade, dubious disc, prism scale, deep sea tooth, and deep sea scale in Undella Town
  - Razor fang and razor claw in Giant Chasm (as recurring hidden item on a suspicious rock)
- Changed trade and time based evolutions
  - Kadabra to Alakazam at level 32
  - Machoke to Machamp at level 40
  - Graveler to Golem, Haunter to Gengar, Boldore to Gigalith, and Gurdurr to Conceldurr at level 37
  - Karrablast to Escavalier and Shelmet to Accelgor at level 20 with the other one or its evolution in your team
  - Eevee to Espeon/Umbreon using a sun/moon stone
  - Poliwhirl to Politoed and Slowpoke to Slowking at level up while holding a king's rock
  - Onix to Steelix and Scyther to Scixor at level up while holding a metal coat
  - Rhydon to Rhyperior at level up while holding a protector
  - Seadra to kingdra at level up while holding a dragon scale
  - Electabuzz to Electivier at level up while holding an electirizer
  - Magmar to Magmortar at level up while holding a magmarizer
  - Porygon to Porygon2 at level up while holding an upgrade
  - Porygon2 to Porygon-Z at level up while holding a dubious disc
  - Feebas to Milotic at level up while holding a prism scale (also removed the contest based evolution)
  - Dusclops to Dusknoir at level up while holding a reaper cloth
  - Clamperl to Huntail/Gorebyss at level up while holding a deep sea tooth/scale
  - Gligar to Gliscor at level up while holding a razor fang (at any time)
  - Sneasel to Weavile at level up while holding a razor claw (at any time)
  - Happiny to Chansey at level up while an oval stone (at any time)
  - Budew to Roselia, Chingling to Chimeco, and Riolu to Lucario at level up with high friendship (at any time)
- Added an NPC to Nimbasa City that can change the weather (if `Season Control` is not `vanilla`)
- Added an NPC to Castelia City that checks for the completion of the TM/HM hunt goal
- Added an NPC to Accumula Town that resets static encounters (including gift and trade encounters)
- Made certain events requiring a specific pokémon in your party accept any pokémon of that species
  - Obtaining Zorua / Zoroark using any Celebi / Entei, Raikou, and Suicune
  - Receiving an item in Lacunosa Town / P2 Laboratory for showing any Shaymin / Genesect
- Made certain time based events available all the time
  - The Musharna at Dreamyard now appears every day instead of only on Friday
  - The Munchlax trade in Undella Town is now available during all seasons
  - Time based items in Lacunosa Town and Café Warehouse are now obtainable all the time
- Prevented gym events from being disabled when beating the gym leader
- The grunt at Pokémon League teleporting you to N's castle now stays even after defeating Ghetsis
  - This also makes the fights against N and Ghetsis repeatable

#### Technicalities
- Removed some ItemSub commands (to not lose key items)
- Changed most HasBadge and AddBadge commands to checking and setting a custom flag
- Changed certain items' data
  - Unused key items and the Rage Candy Bar are now permanently in your bag
- Added badges, seasons, and "AP Item" as virtual items, i.e. you can collect them, but they won't go into your bag
- Changed all overworld, hidden, and npc items to give "AP Item" instead of their vanilla items
- Added a debug menu to the PC help menu

### APWorld

- TODO TODO TODO
- Roadmap
- Changelog
- Credits
- Item data: Bag items and badges
- Location data: Dexsanity
- Encounter data: Regions, slots
- Species data

### Client
