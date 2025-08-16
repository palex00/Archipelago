# Important stuff

- inspect bizhawk 2.10
- dig with seasons patch crashes the game
- fix repeatable/resetting locations, some hidden items seem to not be checkable immediately
- add missing forms

# For 0.2.0

- actually use slot data and datapackage from network, playername still per global var kept alive, if not found then prompt to enter playername
- fisherman in village bridge and lady in driftveil city, write fixed species/tm into rom
- "Challenger's Cave - B1F near stairs to 1F" is actually hidden item
- make tms deprioritized

# Not urgent

- look through scripts and remove space checking for specific items
- ev feathers falsely saying "last one"?
- fix evo method ids
- restructure surf/strength/... species to be lookups into one whole catchable_species set
- find a way to prevent softlocks in shuffle tms/hms
- more inclusion rules
- complete levelup movesets
- advertise on ds romhacking servers
- merge wild encounter events with same species
- make simple script compiler, use for starting season, season npc vanish, tmhm hunt npc vanish, and other future stuff
- change catchable_dex_form to catchable_species in location generation
- change rules dict to being filled on the way
- trigger goal before credits
- organize imports for type hints behind TYPE_CHECKING

# Singular reports, cannot recreate

- not receiving key items?
- scientist nathan no text after battle?
- ranger clause talking french after battle?
