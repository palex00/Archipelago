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
    