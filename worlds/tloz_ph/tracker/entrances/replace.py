import os
import json

base_dir = r"C:\Users\palex\Desktop\Archipelago\Archipelago\worlds\tloz_ph\tracker\entrances"

replacements = {
    "Ember Port House Exit": "Abandoned House Exit",
    "Bannan Salvatore Cave": "Bannan East Cave",
    "Bannan Wayfarer Cave": "Bannan West Cave",
    "Bannan Hut": "Bannan West Hut",
    "Unnamed Entrance 251": "Boulder Tunnel Drop",
    "Cannon Eddo Exit": "Eddo's Exit",
    "Ember Astrid's House": "Ember West Astrid's House",
    "Ember Kayo's House": "Ember West Kayo's House",
    "Ember Port House": "Ember West Port House",
    "Mercay Geozard Cave North Exit": "Eye Bridge Cave North Exit",
    "Mercay Geozard Cave South Exit": "Eye Bridge Cave South Exit",
    "Frost Above Temple SE": "Frost NE Above Temple SE",
    "Frost Above Temple SW": "Frost NE Above Temple SW",
    "Frost Enter Temple": "Frost NE Enter Temple",
    "Frost Field Lower North": "Frost SE Lower North",
    "Frost Field Upper NE": "Frost SE Upper NE",
    "Frost Field Upper NW": "Frost SE Upper NW",
    "Frost Cave East Exit": "Frozen Cave East Exit",
    "Frost Cave West Exit": "Frozen Cave West Exit",
    "Ruins Rupee Cave Exit": "Grassy Rupee Cave Exit",
    "Bannan Cave East Exit": "Keese Passage East Exit",
    "Bannan Cave West Exit": "Keese Passage Exit",
    "Freedle Tunnel East": "Long Bridge Cave East",
    "Freedle Tunnel West": "Long Bridge Cave West",
    "IotD Cave East Exit": "McNey's Cave East Exit",
    "Aquanine Cave Secret Cave": "McNey's Cave Secret Cave",
    "Aquanine Cave West": "McNey's Cave West",
    "Molida Cliff South": "Molida North Cliff South",
    "Molida Cliff Staircase": "Molida North Cliff Staircase",
    "Molida Enter Temple": "Molida North Enter Temple",
    "Molida Cave": "Molida South Cave",
    "Molida Cliff North": "Molida South Cliff North",
    "Molida Port House": "Molida South Ocara's House",
    "Molida Potato's House": "Molida South Potato's House",
    "Molida Romanos' House": "Molida South Romanos' House",
    "Molida Shop": "Molida South Shop",
    "Mountain Passage Lower Exit": "Mountain Passage 1F Exit",
    "Mountain Passage Lower Staircase": "Mountain Passage 1F Staircase",
    "Mountain Passage Upper Exit": "Mountain Passage 2F Exit",
    "Mountain Passage Upper Staircase": "Mountain Passage 2F Staircase",
    "Molida Port House Exit": "Ocara's House Exit",
    "Octo Cave East": "Octorok Cave East",
    "Octo Cave West": "Octorok Cave West",
    "Ruins Geozard Cave East": "Sandy Geozard Cave East",
    "Ruins Geozard Cave West": "Sandy Geozard Cave West",
    "Shovel Cave Exit": "Shovel Hideout Exit",
    "Spirit Cave Exit": "Spirit Shrine Exit",
    "IotD Rupee Cave Exit": "Stone Treasure Cave Exit",
    "Molida Cave Back Cave": "Sun Lake Cave Back Cave",
    "Molida Cave Bomb Cave": "Sun Lake Cave Bomb Cave",
    "Unnamed Entrance 107": "Sun Lake Cave Chest Drop",
    "Molida Cave Exit": "Sun Lake Cave Exit",
    "Molida Cave Geozard Cave": "Sun Lake Cave Geozard Cave",
    "Unnamed Entrance 105": "Sun Lake Cave South Drop",
    "Molida Cave Staircase": "Sun Lake Cave Staircase",
    "Molida Cave Sun Staircase": "Sun Lake Cave Sun Staircase",
    "Gust Hideout Exit": "Tiled Hideout Exit",
}

found = {key: False for key in replacements}

def replace_strings(obj):
    if isinstance(obj, dict):
        return {replace_strings(k): replace_strings(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [replace_strings(i) for i in obj]
    if isinstance(obj, str):
        if obj in replacements:
            found[obj] = True
            return replacements[obj]
    return obj

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                data = f.read()
            
            for old, new in replacements.items():
                if f'"{old}"' in data:
                    found[old] = True
                    data = data.replace(f'"{old}"', f'"{new}"')
            
            new_data = data
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_data)

for key, was_found in found.items():
    if not was_found:
        print(f"Not found: {key}")
