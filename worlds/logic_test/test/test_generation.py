"""End-to-end tests for the Logic Test harness.

These drive a full two-slot generation (under-test game = player 1, Logic Test
= player 2) the same way real usage does, so they're heavier than a typical unit
test. They assert Logic Test reproduces the under-test spheres, places keys
correctly, keeps the seed beatable, and is deterministic.
"""

import logging
import unittest
from argparse import Namespace

import worlds
from BaseClasses import PlandoOptions
from Main import main as ERmain

from ..pass_a import compute_spheres

UT_GAME = "Pokemon Emerald"
LOGIC_TEST_GAME = "Logic Test"
SEED = 12345


def _build_args(player_games, overrides=None):
    """Build a Main.main args Namespace for the given ordered list of game names,
    using each game's default options. ``overrides`` maps player -> {option: value}."""
    reg = worlds.AutoWorldRegister.world_types
    overrides = overrides or {}
    args = Namespace()
    for player, game in enumerate(player_games, 1):
        world_type = reg[game]
        player_overrides = overrides.get(player, {})
        unknown = set(player_overrides) - set(world_type.options_dataclass.type_hints)
        if unknown:
            raise ValueError(f"unknown option overrides for {game}: {sorted(unknown)}")
        for key, option in world_type.options_dataclass.type_hints.items():
            current = getattr(args, key, {})
            value = player_overrides[key] if key in player_overrides else option.default
            current[player] = option.from_any(value)
            setattr(args, key, current)

    count = len(player_games)
    args.multi = count
    args.game = {p: g for p, g in enumerate(player_games, 1)}
    args.name = {p: f"P{p}" for p in range(1, count + 1)}
    args.sprite = {p: None for p in range(1, count + 1)}
    args.sprite_pool = {p: None for p in range(1, count + 1)}
    args.plando = PlandoOptions.from_option_string("bosses, items, connections, texts")
    args.race = False
    args.outputname = None
    args.outputpath = None
    args.skip_output = True
    args.skip_prog_balancing = True
    args.spoiler = 0
    args.spoiler_only = False
    args.csv_output = False
    return args


class TestLogicTestGeneration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.getLogger().setLevel(logging.ERROR)
        args = _build_args([UT_GAME, LOGIC_TEST_GAME])
        cls.multiworld = ERmain(args, seed=SEED)
        cls.world = cls.multiworld.worlds[2]

    def test_has_spheres(self):
        self.assertGreater(len(self.world.spheres), 0, "expected at least one sphere")

    def test_keys_placed_at_under_test_locations(self):
        mw = self.multiworld
        for i, sphere in enumerate(self.world.spheres, start=1):
            for loc_name, loc_player, _item_name, _item_player in sphere:
                loc = mw.get_location(loc_name, loc_player)
                self.assertIsNotNone(loc.item, f"{loc_name} is empty")
                self.assertEqual(loc.item.name, f"KEY_{i}",
                                 f"{loc_name} should hold KEY_{i}")
                self.assertEqual(loc.item.player, self.world.player,
                                 "key should belong to the Logic Test slot")

    def test_under_test_items_held_in_logic_test(self):
        # every Logic Test location is filled with an under-test item (not its own)
        sphere_locs = [loc for region in self.world.sphere_locations for loc in region]
        self.assertEqual(len(sphere_locs), sum(len(s) for s in self.world.spheres))
        for loc in sphere_locs:
            self.assertIsNotNone(loc.item, "Logic Test location left empty")
            self.assertNotEqual(loc.item.player, self.world.player,
                                "Logic Test should hold an under-test item")

    def test_all_under_test_networkable_locations_are_keys(self):
        # every networkable under-test location now holds a Logic Test-owned KEY; none
        # of the under-test's own real items remain in its world.
        for loc in self.multiworld.get_filled_locations(1):
            if loc.address is not None:
                self.assertEqual(loc.item.player, self.world.player,
                                 f"{loc.name} should hold a Logic Test KEY, not {loc.item}")
                self.assertTrue(loc.item.name.startswith("KEY_"),
                                f"{loc.name} should hold a KEY, holds {loc.item.name}")

    def test_item_pool_balanced_and_beatable(self):
        # generation getting this far already proves the pool balanced (no FillError)
        self.assertTrue(self.multiworld.can_beat_game(), "generated seed is not beatable")


class TestLogicTestPriorityLocations(unittest.TestCase):
    """Priority (and early) fill locks its locations, which compute_spheres must NOT
    treat as game-fixed placements. Otherwise those locations get no KEY and the outer
    fill drops real under-test items into them (regression guard)."""

    PRIORITY = ["Artisan Cave 1F - Item", "Artisan Cave B1F - Item", "Route 102 - Item"]

    @classmethod
    def setUpClass(cls):
        logging.getLogger().setLevel(logging.ERROR)
        args = _build_args([UT_GAME, LOGIC_TEST_GAME],
                           overrides={1: {"priority_locations": cls.PRIORITY}})
        cls.multiworld = ERmain(args, seed=SEED)
        cls.world = cls.multiworld.worlds[2]

    def test_priority_locations_hold_keys(self):
        for name in self.PRIORITY:
            loc = self.multiworld.get_location(name, 1)
            self.assertEqual(loc.item.player, self.world.player,
                             f"{name} should hold a Logic Test KEY, holds {loc.item}")
            self.assertTrue(loc.item.name.startswith("KEY_"),
                            f"{name} should hold a KEY, holds {loc.item.name}")

    def test_no_real_items_leak_into_under_test(self):
        for loc in self.multiworld.get_filled_locations(1):
            if loc.address is not None:
                self.assertEqual(loc.item.player, self.world.player,
                                 f"{loc.name} leaked a real item: {loc.item}")

    def test_beatable(self):
        self.assertTrue(self.multiworld.can_beat_game(), "generated seed is not beatable")


class TestLogicTestUnreachableMarkers(unittest.TestCase):
    """Under minimal accessibility the model strands some locations (no sphere record).
    pre_fill must lock a marker there, never leave a real item, and every marker must
    sit on a location that is unreachable in progression (so a pickup signals a leak)."""

    PRIORITY = ["Artisan Cave 1F - Item", "Artisan Cave B1F - Item", "Route 102 - Item"]
    MARKER = "Logic Test Unreachable Marker"

    @classmethod
    def setUpClass(cls):
        logging.getLogger().setLevel(logging.ERROR)
        args = _build_args([UT_GAME, LOGIC_TEST_GAME],
                           overrides={1: {"accessibility": "minimal",
                                          "priority_locations": cls.PRIORITY}})
        cls.multiworld = ERmain(args, seed=55555)

    def _reachable(self):
        reached = set()
        for wave in self.multiworld.get_spheres():
            if not wave:
                break  # empty set precedes the unreachable-locations set
            reached.update((loc.name, loc.player) for loc in wave)
        return reached

    def test_no_real_items_leak(self):
        # every networkable under-test location holds a Logic Test KEY or a marker
        for loc in self.multiworld.get_filled_locations(1):
            if loc.address is not None:
                self.assertEqual(loc.item.player, 2, f"{loc.name} leaked a real item: {loc.item}")
                self.assertTrue(loc.item.name.startswith("KEY_") or loc.item.name == self.MARKER,
                                f"{loc.name} holds {loc.item.name}")

    def test_markers_present_and_unreachable(self):
        markers = [loc for loc in self.multiworld.get_filled_locations(1)
                   if loc.address is not None and loc.item.name == self.MARKER]
        self.assertGreater(len(markers), 0, "expected markers on this stranded seed")
        reached = self._reachable()
        for loc in markers:
            self.assertNotIn((loc.name, loc.player), reached,
                             f"marker on reachable location {loc.name}; would be a false positive")

    def test_beatable(self):
        self.assertTrue(self.multiworld.can_beat_game(), "generated seed is not beatable")


class TestLogicTestDeterminism(unittest.TestCase):
    def test_pass_a_spheres_stable(self):
        """Two solo generations of the under-test game with the same seed must
        produce identical sphere location lists (guards the determinism the
        harness relies on)."""
        logging.getLogger().setLevel(logging.ERROR)

        def solo_spheres():
            args = _build_args([UT_GAME])
            mw = ERmain(args, seed=SEED)
            # sort within each sphere: compute_spheres iterates a set, so
            # intra-sphere order is not stable (and is irrelevant to the harness).
            return [sorted(sphere) for sphere in compute_spheres(mw)]

        first = solo_spheres()
        second = solo_spheres()
        self.assertEqual(first, second, "under-test sphere structure is not deterministic")


class TestCountEventsOption(unittest.TestCase):
    def test_option_registered_default_off(self):
        opts = worlds.AutoWorldRegister.world_types[LOGIC_TEST_GAME].options_dataclass.type_hints
        self.assertIn("count_events", opts)
        self.assertFalse(bool(opts["count_events"].default), "count_events should default off")

    def test_events_off_is_coarser(self):
        logging.getLogger().setLevel(logging.ERROR)
        mw = ERmain(_build_args([UT_GAME]), seed=SEED)
        on = compute_spheres(mw, count_events=True)
        off = compute_spheres(mw, count_events=False)
        self.assertLess(len(off), len(on), "events-off should produce fewer (coarser) spheres")
        # both must distribute the same total networkable items
        self.assertEqual(sum(len(s) for s in on), sum(len(s) for s in off))

    def test_events_off_generates_beatable(self):
        # count_events=off closes over events between spheres (they never cause
        # a boundary), which preserves dependency order and stays solvable.
        logging.getLogger().setLevel(logging.ERROR)
        args = _build_args([UT_GAME, LOGIC_TEST_GAME], overrides={2: {"count_events": 0}})
        mw = ERmain(args, seed=SEED)
        self.assertTrue(mw.can_beat_game(), "count_events=off seed should be beatable")
        self.assertGreater(len(mw.worlds[2].spheres), 0)


class TestLockedPlacementsLockStep(unittest.TestCase):
    """Locked in-game placements (here Emerald's shuffled badges/HMs, pre-placed with
    lock=True) are never gated by the Logic Test, so the model must collect them via
    closure. Otherwise a location gated only by a locked item is recorded one sphere
    late and its KEY is reachable in play before the previous sphere completes (a
    false logic leak; regression guard)."""

    @classmethod
    def setUpClass(cls):
        logging.getLogger().setLevel(logging.ERROR)
        args = _build_args([UT_GAME, LOGIC_TEST_GAME],
                           overrides={1: {"badges": "shuffle", "hms": "shuffle"},
                                      2: {"count_events": 0}})
        cls.multiworld = ERmain(args, seed=SEED)
        cls.world = cls.multiworld.worlds[2]

    def test_fixture_has_locked_networkable_placements(self):
        # the guard's premise: the under-test slot keeps some of its own items at
        # locked, addressed locations (shuffled badges/HMs); everything else got a KEY
        fixed = [loc for loc in self.multiworld.get_filled_locations(1)
                 if type(loc.address) is int and loc.item.player == 1]
        self.assertGreater(len(fixed), 0, "fixture lost its locked badge/HM placements")

    def test_gated_play_is_lock_step(self):
        self.assertGreater(len(self.world.spheres), 0)
        key_sphere = {(loc_name, loc_player): i
                      for i, sphere in enumerate(self.world.spheres, start=1)
                      for (loc_name, loc_player, _in, _ip) in sphere}
        required = {i: len(s) for i, s in enumerate(self.world.spheres, start=1)}
        seen = {i: 0 for i in required}
        # get_spheres yields each wave before collecting it, i.e. real play order
        for wave in self.multiworld.get_spheres():
            if not wave:
                break  # empty set precedes the unreachable-locations set
            keyed = [(loc, key_sphere.get((loc.name, loc.player))) for loc in wave]
            for loc, i in keyed:
                if i is None:
                    continue
                for j in range(1, i):
                    self.assertEqual(
                        seen[j], required[j],
                        f"KEY_{i} location '{loc.name}' reachable with sphere {j} "
                        f"incomplete ({seen[j]}/{required[j]})")
            for _loc, i in keyed:
                if i is not None:
                    seen[i] += 1
        self.assertEqual(seen, required, "gated play did not reach every KEY location")


class TestPlayerOrdering(unittest.TestCase):
    def test_under_test_as_player_two(self):
        # Logic Test as player 1, under-test as player 2. The RNG recompute must
        # reproduce the under-test structure from its slot number, so keys land
        # correctly and the seed stays beatable regardless of YAML order.
        logging.getLogger().setLevel(logging.ERROR)
        mw = ERmain(_build_args([LOGIC_TEST_GAME, UT_GAME]), seed=SEED)
        lt = mw.worlds[1]
        self.assertGreater(len(lt.spheres), 0)
        for i, sphere in enumerate(lt.spheres, start=1):
            for loc_name, loc_player, _item_name, _item_player in sphere:
                loc = mw.get_location(loc_name, loc_player)
                self.assertEqual(loc.item.name, f"KEY_{i}")
                self.assertEqual(loc.item.player, 1)
        self.assertTrue(mw.can_beat_game(), "reversed-order seed should be beatable")


class TestMultipleUnderTest(unittest.TestCase):
    def test_two_under_test_games(self):
        # One Logic Test mirroring the overall spheres of two under-test slots.
        logging.getLogger().setLevel(logging.ERROR)
        mw = ERmain(_build_args([UT_GAME, UT_GAME, LOGIC_TEST_GAME]), seed=SEED)
        lt = mw.worlds[3]
        self.assertGreater(len(lt.spheres), 0)
        # spheres should reference both under-test slots
        loc_players = {loc_player for sphere in lt.spheres
                       for (_ln, loc_player, _in, _ip) in sphere}
        self.assertEqual(loc_players, {1, 2}, "overall spheres should span both under-test slots")
        # every recorded location holds the right KEY, owned by the Logic Test
        for i, sphere in enumerate(lt.spheres, start=1):
            for loc_name, loc_player, _item_name, _item_player in sphere:
                loc = mw.get_location(loc_name, loc_player)
                self.assertEqual(loc.item.name, f"KEY_{i}")
                self.assertEqual(loc.item.player, 3)
        self.assertTrue(mw.can_beat_game(), "two-slot under-test seed should be beatable")
