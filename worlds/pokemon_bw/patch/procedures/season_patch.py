from typing import TYPE_CHECKING

from ndspy.rom import NintendoDSRom
from ndspy.code import saveOverlayTable
import pkgutil

from .. import otpp

if TYPE_CHECKING:
    from ...rom import PokemonBlackPatch


def patch_black(rom: NintendoDSRom, world_package: str, bw_patch_instance: "PokemonBlackPatch") -> None:
    _patch(rom, pkgutil.get_data(world_package, "patch/seasons_otpp/ov20_B_decomp"))


def patch_white(rom: NintendoDSRom, world_package: str, bw_patch_instance: "PokemonBlackPatch") -> None:
    _patch(rom, pkgutil.get_data(world_package, "patch/seasons_otpp/ov20_W_decomp"))


def _patch(rom: NintendoDSRom, otpp_patch: bytes) -> None:
    overlay_table = rom.loadArm9Overlays([20])
    ov20 = overlay_table[20]
    ov20.data = otpp.patch(ov20.data, otpp_patch)
    rom.files[ov20.fileID] = ov20.save(compress=True)
    rom.arm9OverlayTable = saveOverlayTable(overlay_table)

