import math
import hashlib
import itertools
import struct
import os
# import bsdiff4
import pkgutil
import unicodedata

from typing import TYPE_CHECKING
import settings
import Utils
from worlds.Files import APDeltaPatch

from . import Items
from .options import Dexsanity

if TYPE_CHECKING:
    from . import PkMnBW


# ROM ADDRESSES
class Addr:
    Pokemon = 0x0
    Items = 0x0
    Seasons = 0x0

