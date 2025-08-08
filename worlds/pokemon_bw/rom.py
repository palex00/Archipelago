import asyncio
import os
import zipfile

import ndspy.rom
import orjson

import Utils
from settings import get_settings
from worlds.Files import APAutoPatchInterface
from typing import TYPE_CHECKING, Any, Dict, Callable

from .patch.procedures import base_patch, season_patch, slot_data

if TYPE_CHECKING:
    from . import PokemonBWWorld


cached_rom: list[ndspy.rom.NintendoDSRom | None] = [None]


async def keep_cache_alive():
    while cached_rom[0] is not None:
        await asyncio.sleep(5)


class PokemonBlackPatch(APAutoPatchInterface):
    game = "Pokemon Black and White"
    bw_patch_version = (0, 1, 0)
    patch_file_ending = ".apblack"
    result_file_ending = ".nds"

    def __init__(self, *args: Any, **kwargs: Any):
        self.world = None
        if "world" in kwargs:
            self.world: "PokemonBWWorld" = kwargs["world"]
        self.files: dict[str, bytes] = {}
        super().__init__(*args, **kwargs)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        super().write_contents(opened_zipfile)

        procedures: list[str] = ["base_patch", "slot_data"]
        if self.world.options.season_control:
            procedures.append("season_patch_"+self.world.options.version.current_key)

        datapackage: dict[str, Any] = {
            "location_name_to_id": self.world.location_name_to_id,
            "item_id_to_name": self.world.item_id_to_name,
        }

        slot_data_dict: dict[str, Any] = {
            "goal": self.world.options.goal.current_key,
            "version": self.world.options.version.current_key,
            "season_control": self.world.options.season_control.current_key,
        }

        opened_zipfile.writestr("procedures.txt", "\n".join(procedures))
        opened_zipfile.writestr("datapackage.json", orjson.dumps(datapackage))
        opened_zipfile.writestr("slot_data.json", orjson.dumps(slot_data_dict))

    def get_manifest(self) -> Dict[str, Any]:
        manifest = super().get_manifest()
        manifest["bw_patch_version"] = self.bw_patch_version
        return manifest

    def patch(self, target: str) -> None:
        self.read()

        slot_data_dict: dict[str, Any] = orjson.loads(self.get_file("slot_data.json"))
        base_data = get_base_rom_bytes(slot_data_dict["version"])

        rom = ndspy.rom.NintendoDSRom(base_data)
        procedures: list[str] = str(self.get_file("procedures.txt"), "utf-8").splitlines()
        for prod in procedures:
            patch_procedures[prod](rom, __name__, self)

        with open(target, 'wb') as f:
            f.write(rom.save(updateDeviceCapacity=True))

        cached_rom[0] = rom
        asyncio.run(keep_cache_alive())

    def read_contents(self, opened_zipfile: zipfile.ZipFile) -> Dict[str, Any]:
        for file in opened_zipfile.namelist():
            if file not in ["archipelago.json"]:
                self.files[file] = opened_zipfile.read(file)

        manifest = super().read_contents(opened_zipfile)
        if manifest["bw_patch_version"] > self.bw_patch_version:
            raise Exception(f"File (BW patch version: {".".join(manifest["bw_patch_version"])} too new "
                            f"for this handler (BW patch version: {self.bw_patch_version}). "
                            f"Please update your apworld.")
        return manifest

    def get_file(self, file: str) -> bytes:
        if file not in self.files:
            self.read()
        return self.files[file]


class PokemonWhitePatch(PokemonBlackPatch):
    patch_file_ending = ".apwhite"


patch_procedures: dict[str, Callable[[ndspy.rom.NintendoDSRom, str, PokemonBlackPatch], None]] = {
    "base_patch": base_patch.patch,
    "season_patch_black": season_patch.patch_black,
    "season_patch_white": season_patch.patch_white,
    "slot_data": slot_data.add_slot_data_file,
}


def get_base_rom_bytes(version: str, file_name: str = "") -> bytes:
    if not file_name:
        file_name = get_base_rom_path(version, file_name)
    with open(file_name, "rb") as file:
        base_rom_bytes = bytes(file.read())
    if version == "black" and base_rom_bytes[:18] != b'POKEMON\x20B\0\0\0IRBO01':
        raise Exception(f"Supplied Base Rom appears to not be an english copy of Pokémon Black Version.")
    if version == "white" and base_rom_bytes[:18] != b'POKEMON\x20W\0\0\0IRAO01':
        raise Exception(f"Supplied Base Rom appears to not be an english copy of Pokémon White Version.")
    return base_rom_bytes


def get_base_rom_path(version: str, file_name: str = "") -> str:
    if not file_name:
        file_name = get_settings()["pokemon_bw_settings"][f"{version}_rom"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name
