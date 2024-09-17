import binascii
import importlib.util
import importlib.machinery
import os
import pkgutil
from collections import defaultdict
from typing import TYPE_CHECKING

from .romTables import ROMWithTables
from . import assembler
from . import mapgen
from . import patches
from .patches import overworld as _
from .patches import dungeon as _
from .patches import entrances as _
from .patches import enemies as _
from .patches import titleScreen as _
from .patches import aesthetics as _
from .patches import music as _
from .patches import core as _
from .patches import phone as _
from .patches import photographer as _
from .patches import owl as _
from .patches import bank3e as _
from .patches import bank3f as _
from .patches import inventory as _
from .patches import witch as _
from .patches import tarin as _
from .patches import fishingMinigame as _
from .patches import softlock as _
from .patches import maptweaks as _
from .patches import chest as _
from .patches import bomb as _
from .patches import rooster as _
from .patches import shop as _
from .patches import trendy as _
from .patches import goal as _
from .patches import hardMode as _
from .patches import weapons as _
from .patches import health as _
from .patches import heartPiece as _
from .patches import droppedKey as _
from .patches import goldenLeaf as _
from .patches import songs as _
from .patches import bowwow as _
from .patches import desert as _
from .patches import reduceRNG as _
from .patches import madBatter as _
from .patches import tunicFairy as _
from .patches import seashell as _
from .patches import instrument as _
from .patches import endscreen as _
from .patches import save as _
from .patches import bingo as _
from .patches import multiworld as _
from .patches import tradeSequence as _
from . import hints

from .patches import bank34
from .utils import formatText
from ..Options import TrendyGame, Palette
from .roomEditor import RoomEditor, Object
from .patches.aesthetics import rgb_to_bin, bin_to_rgb

from .locations.keyLocation import KeyLocation

from BaseClasses import ItemClassification
from ..Locations import LinksAwakeningLocation
from ..Options import TrendyGame, Palette, MusicChangeCondition, BootsControls

if TYPE_CHECKING:
    from .. import LinksAwakeningWorld


# Function to generate a final rom, this patches the rom with all required patches
def generateRom(args, world: "LinksAwakeningWorld"):
    rom_patches = []
    player_names = list(world.multiworld.player_name.values())

    rom = ROMWithTables(args.input_filename, rom_patches)
    rom.player_names = player_names
    pymods = []
    if args.pymod:
        for pymod in args.pymod:
            spec = importlib.util.spec_from_loader(pymod, importlib.machinery.SourceFileLoader(pymod, pymod))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            pymods.append(module)
    for pymod in pymods:
        pymod.prePatch(rom)

    if world.ladxr_settings.gfxmod:
        patches.aesthetics.gfxMod(rom, os.path.join("data", "sprites", "ladx", world.ladxr_settings.gfxmod))

    item_list = [item for item in world.ladxr_logic.iteminfo_list if not isinstance(item, KeyLocation)]

    assembler.resetConsts()
    assembler.const("INV_SIZE", 16)
    assembler.const("wHasFlippers", 0xDB3E)
    assembler.const("wHasMedicine", 0xDB3F)
    assembler.const("wTradeSequenceItem", 0xDB40)  # we use it to store flags of which trade items we have
    assembler.const("wTradeSequenceItem2", 0xDB7F)  # Normally used to store that we have exchanged the trade item, we use it to store flags of which trade items we have
    assembler.const("wSeashellsCount", 0xDB41)
    assembler.const("wGoldenLeaves", 0xDB42)  # New memory location where to store the golden leaf counter
    assembler.const("wCollectedTunics", 0xDB6D)  # Memory location where to store which tunic options are available (and boots)
    assembler.const("wCustomMessage", 0xC0A0)

    # We store the link info in unused color dungeon flags, so it gets preserved in the savegame.
    assembler.const("wLinkSyncSequenceNumber", 0xDDF6)
    assembler.const("wLinkStatusBits", 0xDDF7)
    assembler.const("wLinkGiveItem", 0xDDF8)
    assembler.const("wLinkGiveItemFrom", 0xDDF9)
    assembler.const("wLinkSendItemRoomHigh", 0xDDFA)
    assembler.const("wLinkSendItemRoomLow", 0xDDFB)
    assembler.const("wLinkSendItemTarget", 0xDDFC)
    assembler.const("wLinkSendItemItem", 0xDDFD)

    assembler.const("wZolSpawnCount", 0xDE10)
    assembler.const("wCuccoSpawnCount", 0xDE11)
    assembler.const("wDropBombSpawnCount", 0xDE12)
    assembler.const("wLinkSpawnDelay", 0xDE13)

    #assembler.const("HARDWARE_LINK", 1)
    assembler.const("HARD_MODE", 1 if world.ladxr_settings.hardmode != "none" else 0)

    patches.core.cleanup(rom)
    patches.save.singleSaveSlot(rom)
    patches.phone.patchPhone(rom)
    patches.photographer.fixPhotographer(rom)
    patches.core.bugfixWrittingWrongRoomStatus(rom)
    patches.core.bugfixBossroomTopPush(rom)
    patches.core.bugfixPowderBagSprite(rom)
    patches.core.fixEggDeathClearingItems(rom)
    patches.core.disablePhotoPrint(rom)
    patches.core.easyColorDungeonAccess(rom)
    patches.owl.removeOwlEvents(rom)
    patches.enemies.fixArmosKnightAsMiniboss(rom)
    patches.bank3e.addBank3E(rom, world.multi_key, world.player, player_names)
    patches.bank3f.addBank3F(rom)
    patches.bank34.addBank34(rom, item_list)
    patches.core.removeGhost(rom)
    patches.core.fixMarinFollower(rom)
    patches.core.fixWrongWarp(rom)
    patches.core.alwaysAllowSecretBook(rom)
    patches.core.injectMainLoop(rom)

    from ..Options import ShuffleSmallKeys, ShuffleNightmareKeys

    if world.options.shuffle_small_keys != ShuffleSmallKeys.option_original_dungeon or\
            world.options.shuffle_nightmare_keys != ShuffleNightmareKeys.option_original_dungeon:
        patches.inventory.advancedInventorySubscreen(rom)
    patches.inventory.moreSlots(rom)
    if world.ladxr_settings.witch:
        patches.witch.updateWitch(rom)
    patches.softlock.fixAll(rom)
    patches.maptweaks.tweakMap(rom)
    patches.chest.fixChests(rom)
    patches.shop.fixShop(rom)
    patches.rooster.patchRooster(rom)
    patches.trendy.fixTrendy(rom)
    patches.droppedKey.fixDroppedKey(rom)
    patches.madBatter.upgradeMadBatter(rom)
    patches.tunicFairy.upgradeTunicFairy(rom)
    patches.tarin.updateTarin(rom)
    patches.fishingMinigame.updateFinishingMinigame(rom)
    patches.health.upgradeHealthContainers(rom)
    if world.ladxr_settings.owlstatues in ("dungeon", "both"):
        patches.owl.upgradeDungeonOwlStatues(rom)
    if world.ladxr_settings.owlstatues in ("overworld", "both"):
        patches.owl.upgradeOverworldOwlStatues(rom)
    patches.goldenLeaf.fixGoldenLeaf(rom)
    patches.heartPiece.fixHeartPiece(rom)
    patches.seashell.fixSeashell(rom)
    patches.instrument.fixInstruments(rom)
    patches.seashell.upgradeMansion(rom)
    patches.songs.upgradeMarin(rom)
    patches.songs.upgradeManbo(rom)
    patches.songs.upgradeMamu(rom)
    if world.ladxr_settings.tradequest:
        patches.tradeSequence.patchTradeSequence(rom, world.ladxr_settings.boomerang)
    else:
        # Monkey bridge patch, always have the bridge there.
        rom.patch(0x00, 0x333D, assembler.ASM("bit 4, e\njr Z, $05"), b"", fill_nop=True)
    patches.bowwow.fixBowwow(rom, everywhere=world.ladxr_settings.bowwow != 'normal')
    if world.ladxr_settings.bowwow != 'normal':
        patches.bowwow.bowwowMapPatches(rom)
    patches.desert.desertAccess(rom)
    if world.ladxr_settings.overworld == 'dungeondive':
        patches.overworld.patchOverworldTilesets(rom)
        patches.overworld.createDungeonOnlyOverworld(rom)
    elif world.ladxr_settings.overworld == 'nodungeons':
        patches.dungeon.patchNoDungeons(rom)
    elif world.ladxr_settings.overworld == 'random':
        patches.overworld.patchOverworldTilesets(rom)
        mapgen.store_map(rom, world.ladxr_logic.world.map)
    #if settings.dungeon_items == 'keysy':
    #    patches.dungeon.removeKeyDoors(rom)
    # patches.reduceRNG.slowdownThreeOfAKind(rom)
    patches.reduceRNG.fixHorseHeads(rom)
    patches.bomb.onlyDropBombsWhenHaveBombs(rom)
    if world.options.music_change_condition == MusicChangeCondition.option_always:
        patches.aesthetics.noSwordMusic(rom)
    patches.aesthetics.reduceMessageLengths(rom, world.random)
    patches.aesthetics.allowColorDungeonSpritesEverywhere(rom)
    if world.ladxr_settings.music == 'random':
        patches.music.randomizeMusic(rom, world.random)
    elif world.ladxr_settings.music == 'off':
        patches.music.noMusic(rom)
    # if world.ladxr_settings.noflash:
    patches.aesthetics.removeFlashingLights(rom)
    if world.ladxr_settings.hardmode == "oracle":
        patches.hardMode.oracleMode(rom)
    elif world.ladxr_settings.hardmode == "hero":
        patches.hardMode.heroMode(rom)
    elif world.ladxr_settings.hardmode == "ohko":
        patches.hardMode.oneHitKO(rom)
    if world.ladxr_settings.superweapons:
        patches.weapons.patchSuperWeapons(rom)
    if world.ladxr_settings.textmode == 'fast':
        patches.aesthetics.fastText(rom)
    if world.ladxr_settings.textmode == 'none':
        patches.aesthetics.fastText(rom)
        patches.aesthetics.noText(rom)
    if not world.ladxr_settings.nagmessages:
        patches.aesthetics.removeNagMessages(rom)
    if world.ladxr_settings.lowhpbeep == 'slow':
        patches.aesthetics.slowLowHPBeep(rom)
    if world.ladxr_settings.lowhpbeep == 'none':
        patches.aesthetics.removeLowHPBeep(rom)
    if 0 <= int(world.ladxr_settings.linkspalette):
        patches.aesthetics.forceLinksPalette(rom, int(world.ladxr_settings.linkspalette))
    if args.romdebugmode:
        # The default rom has this build in, just need to set a flag and we get this save.
        rom.patch(0, 0x0003, "00", "01")

    if world.ladxr_settings.hpmode == 'inverted':
        patches.health.setStartHealth(rom, 9)
    elif world.ladxr_settings.hpmode == '1':
        patches.health.setStartHealth(rom, 1)

    patches.inventory.songSelectAfterOcarinaSelect(rom)
    if world.ladxr_settings.quickswap == 'a':
        patches.core.quickswap(rom, 1)
    elif world.ladxr_settings.quickswap == 'b':
        patches.core.quickswap(rom, 0)

    patches.core.addBootsControls(rom, world.options.boots_controls)


    world_setup = world.ladxr_logic.world_setup

    JUNK_HINT = 0.33
    RANDOM_HINT= 0.66
    # USEFUL_HINT = 1.0
    # TODO: filter events, filter unshuffled keys
    all_items = world.multiworld.get_items()
    our_items = [item for item in all_items
                 if item.player == world.player
                 and item.location
                 and item.code is not None
                 and item.location.show_in_spoiler]
    our_useful_items = [item for item in our_items if ItemClassification.progression in item.classification]

    def gen_hint():
        if not world.options.in_game_hints:
            return 'Hints are disabled!'
        chance = world.random.uniform(0, 1)
        if chance < JUNK_HINT:
            return None
        elif chance < RANDOM_HINT:
            location = world.random.choice(our_items).location
        else: # USEFUL_HINT
            location = world.random.choice(our_useful_items).location

        if location.item.player == world.player:
            name = "Your"
        else:
            name = f"{world.multiworld.player_name[location.item.player]}'s"
            # filter out { and } since they cause issues with string.format later on
            name = name.replace("{", "").replace("}", "")

        if isinstance(location, LinksAwakeningLocation):
            location_name = location.ladxr_item.metadata.name
        else:
            location_name = location.name

        hint = f"{name} {location.item.name} is at {location_name}"
        if location.player != world.player:
            # filter out { and } since they cause issues with string.format later on
            player_name = world.multiworld.player_name[location.player].replace("{", "").replace("}", "")
            hint += f" in {player_name}'s world"

        # Cap hint size at 85
        # Realistically we could go bigger but let's be safe instead
        hint = hint[:85]

        return hint

    hints.addHints(rom, world.random, gen_hint)

    if world_setup.goal == "raft":
        patches.goal.setRaftGoal(rom)
    elif world_setup.goal in ("bingo", "bingo-full"):
        patches.bingo.setBingoGoal(rom, world_setup.bingo_goals, world_setup.goal)
    elif world_setup.goal == "seashells":
        patches.goal.setSeashellGoal(rom, 20)
    else:
        patches.goal.setRequiredInstrumentCount(rom, world_setup.goal)

    # Patch the generated logic into the rom
    patches.chest.setMultiChest(rom, world_setup.multichest)
    if world.ladxr_settings.overworld not in {"dungeondive", "random"}:
        patches.entrances.changeEntrances(rom, world_setup.entrance_mapping)
    for spot in item_list:
        if spot.item and spot.item.startswith("*"):
            spot.item = spot.item[1:]
        mw = None
        if spot.item_owner != spot.location_owner:
            mw = spot.item_owner
            if mw > 100:
                # There are only 101 player name slots (99 + "The Server" + "another world"), so don't use more than that
                mw = 100
        spot.patch(rom, spot.item, multiworld=mw)
    patches.enemies.changeBosses(rom, world_setup.boss_mapping)
    patches.enemies.changeMiniBosses(rom, world_setup.miniboss_mapping)

    if not args.romdebugmode:
        patches.core.addFrameCounter(rom, len(item_list))

    patches.core.warpHome(rom)  # Needs to be done after setting the start location.
    patches.titleScreen.setRomInfo(rom, world.multi_key, world.multiworld.seed_name, world.ladxr_settings,
                                   world.player_name, world.player)
    if world.options.ap_title_screen:
        patches.titleScreen.setTitleGraphics(rom)
    patches.endscreen.updateEndScreen(rom)
    patches.aesthetics.updateSpriteData(rom)
    if args.doubletrouble:
        patches.enemies.doubleTrouble(rom)

    if world.options.text_shuffle:
        excluded_ids = [
            # Overworld owl statues
            0x1B6, 0x1B7, 0x1B8, 0x1B9, 0x1BA, 0x1BB, 0x1BC, 0x1BD, 0x1BE, 0x22D,

            # Dungeon owls
            0x288, 0x280,  # D1
            0x28A, 0x289, 0x281,  # D2
            0x282, 0x28C, 0x28B,  # D3
            0x283,  # D4
            0x28D, 0x284,  # D5
            0x285, 0x28F, 0x28E,  # D6
            0x291, 0x290, 0x286,  # D7
            0x293, 0x287, 0x292,  # D8
            0x263,  # D0

            # Hint books
            0x267,  # color dungeon
            0x200, 0x201,
            0x202, 0x203,
            0x204, 0x205,
            0x206, 0x207,
            0x208, 0x209,
            0x20A, 0x20B,
            0x20C,
            0x20D, 0x20E,
            0x217, 0x218, 0x219, 0x21A,

            # Goal sign
            0x1A3,

            # Signpost maze
            0x1A9, 0x1AA, 0x1AB, 0x1AC, 0x1AD,

            # Prices
            0x02C, 0x02D, 0x030, 0x031, 0x032, 0x033, # Shop items
            0x03B, # Trendy Game
            0x045, # Fisherman
            0x018, 0x019, # Crazy Tracy
            0x0DC, # Mamu
            0x0F0, # Raft ride
        ]
        excluded_texts = [ rom.texts[b_id] for b_id in excluded_ids]
        buckets = defaultdict(list)
        # For each ROM bank, shuffle text within the bank
        for n, data in enumerate(rom.texts._PointerTable__data):
            # Don't muck up which text boxes are questions and which are statements
            if type(data) != int and data and data != b'\xFF' and data not in excluded_texts:
                buckets[(rom.texts._PointerTable__banks[n], data[len(data) - 1] == 0xfe)].append((n, data))
        for bucket in buckets.values():
            # For each bucket, make a copy and shuffle
            shuffled = bucket.copy()
            world.random.shuffle(shuffled)
            # Then put new text in
            for bucket_idx, (orig_idx, data) in enumerate(bucket):
                rom.texts[shuffled[bucket_idx][0]] = data


    if world.options.trendy_game != TrendyGame.option_normal:

        # TODO: if 0 or 4, 5, remove inaccurate conveyor tiles


        room_editor = RoomEditor(rom, 0x2A0)

        if world.options.trendy_game == TrendyGame.option_easy:
            # Set physics flag on all objects
            for i in range(0, 6):
                rom.banks[0x4][0x6F1E + i -0x4000] = 0x4
        else:
            # All levels
            # Set physics flag on yoshi
            rom.banks[0x4][0x6F21-0x4000] = 0x3
            # Add new conveyor to "push" yoshi (it's only a visual)
            room_editor.objects.append(Object(5, 3, 0xD0))

            if world.options.trendy_game >= TrendyGame.option_harder:
                """
                Data_004_76A0::
                    db   $FC, $00, $04, $00, $00

                Data_004_76A5::
                    db   $00, $04, $00, $FC, $00
                """
                speeds = {
                    TrendyGame.option_harder: (3, 8),
                    TrendyGame.option_hardest: (3, 8),
                    TrendyGame.option_impossible: (3, 16),
                }
                def speed():
                    return world.random.randint(*speeds[world.options.trendy_game])
                rom.banks[0x4][0x76A0-0x4000] = 0xFF - speed()
                rom.banks[0x4][0x76A2-0x4000] = speed()
                rom.banks[0x4][0x76A6-0x4000] = speed()
                rom.banks[0x4][0x76A8-0x4000] = 0xFF - speed()
                if world.options.trendy_game >= TrendyGame.option_hardest:
                    rom.banks[0x4][0x76A1-0x4000] = 0xFF - speed()
                    rom.banks[0x4][0x76A3-0x4000] = speed()
                    rom.banks[0x4][0x76A5-0x4000] = speed()
                    rom.banks[0x4][0x76A7-0x4000] = 0xFF - speed()

            room_editor.store(rom)
            # This doesn't work, you can set random conveyors, but they aren't used
            # for x in range(3, 9):
            #     for y in range(1, 5):
            #         room_editor.objects.append(Object(x, y, 0xCF + rnd.randint(0, 3)))

    # Attempt at imitating gb palette, fails
    if False:
        gb_colors = [
            [0x0f, 0x38, 0x0f],
            [0x30, 0x62, 0x30],
            [0x8b, 0xac, 0x0f],
            [0x9b, 0xbc, 0x0f],
        ]
        for color in gb_colors:
            for channel in range(3):
                color[channel] = color[channel] * 31 // 0xbc

    if world.options.warp_improvements:
        patches.core.addWarpImprovements(rom, world.options.additional_warp_points)

    palette = world.options.palette
    if palette != Palette.option_normal:
        ranges = {
            # Object palettes
            # Overworld palettes
            # Dungeon palettes
            # Interior palettes
            "code/palettes.asm 1": (0x21, 0x1518, 0x34A0),
            # Intro/outro(?)
            # File select
            # S+Q
            # Map
            "code/palettes.asm 2": (0x21, 0x3536, 0x3FFE),
            # Used for transitioning in and out of forest
            "backgrounds/palettes.asm": (0x24, 0x3478, 0x3578),
            # Haven't yet found menu palette
        }

        for name, (bank, start, end) in ranges.items():
            def clamp(x, min, max):
                if x < min:
                    return min
                if x > max:
                    return max
                return x

            for address in range(start, end, 2):
                packed = (rom.banks[bank][address + 1] << 8) | rom.banks[bank][address]
                r,g,b = bin_to_rgb(packed)

                # 1 bit
                if palette == Palette.option_1bit:
                    r &= 0b10000
                    g &= 0b10000
                    b &= 0b10000
                # 2 bit
                elif palette == Palette.option_1bit:
                    r &= 0b11000
                    g &= 0b11000
                    b &= 0b11000
                # Invert
                elif palette == Palette.option_inverted:
                    r = 31 - r
                    g = 31 - g
                    b = 31 - b
                # Pink
                elif palette == Palette.option_pink:
                    r = r // 2
                    r += 16
                    r = int(r)
                    r = clamp(r, 0, 0x1F)
                    b = b // 2
                    b += 16
                    b = int(b)
                    b = clamp(b, 0, 0x1F)
                elif palette == Palette.option_greyscale:
                    # gray=int(0.299*r+0.587*g+0.114*b)
                    gray = (r + g + b) // 3
                    r = g = b = gray

                packed = rgb_to_bin(r, g, b)
                rom.banks[bank][address] = packed & 0xFF
                rom.banks[bank][address + 1] = packed >> 8

    SEED_LOCATION = 0x0134
    # Patch over the title
    assert(len(world.multi_key) == 12)
    rom.patch(0x00, SEED_LOCATION, None, binascii.hexlify(world.multi_key))

    for pymod in pymods:
        pymod.postPatch(rom)

    return rom
