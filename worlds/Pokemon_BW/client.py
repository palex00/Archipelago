#importing libraries
from typing import TYPE_CHECKING, Dict, Set, Tuple, List
import struct

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import asyncio
import Utils
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess


if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object

class PkMnBWClient(BizHawkClient):
    game = "Pokemon Black and White"
    system = "NDS"
    patch_suffix = ".apbw"
    local_checked_locations: Set[int]
    goal : int
    ram_mem_domain = "Main RAM"
    goal_complete = False

    def __init__(self) -> None:
            super().__init__()
            self.local_checked_locations = set()
            self.local_set_events = {}
            self.local_found_key_items = {}
            self.rom_slot_name = None
            self.seed_verify = False
            self.eUsed = []
            self.room = 0
            self.local_events = []

    async def update_received_items(self, ctx: "BizHawkClientContext", received_items_offset, received_index,
                                    i) -> None:
        await bizhawk.write(
            ctx.bizhawk_ctx,
            [
                (received_items_offset, [(received_index + i + 1) // 0x100, (received_index + i + 1) % 0x100],
                 self.ram_mem_domain),
            ]
        )