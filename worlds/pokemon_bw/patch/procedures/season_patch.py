import io
from typing import NamedTuple, TYPE_CHECKING
from zipfile import ZipFile

from ndspy.rom import NintendoDSRom
from ndspy.narc import NARC
import pkgutil

from .. import otpp

if TYPE_CHECKING:
    from ...rom import PokemonBWPatch


def patch_black(rom: NintendoDSRom, world_package: str, bw_patch_instance: PokemonBWPatch) -> None:
    _patch(rom, pkgutil.get_data(world_package, "patch/seasons_otpp/ov20_B"))


def patch_white(rom: NintendoDSRom, world_package: str, bw_patch_instance: PokemonBWPatch) -> None:
    _patch(rom, pkgutil.get_data(world_package, "patch/seasons_otpp/ov20_W"))


def _patch(rom: NintendoDSRom, otpp_patch: bytes) -> None:
    ov20 = rom.loadArm9Overlays([20])[20]
    ov20.data = otpp.patch(ov20.data, otpp_patch)
    rom.files[ov20.fileID] = ov20.save(compress=True)

