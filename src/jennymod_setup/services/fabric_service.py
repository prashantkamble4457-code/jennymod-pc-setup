"""Wraps Fabric Loader detection / install for JennyMod requirements."""
from __future__ import annotations

import subprocess
from pathlib import Path


class FabricService:
    def __init__(self, minecraft_dir: Path):
        self.minecraft_dir = minecraft_dir
        self.versions_dir = minecraft_dir / "versions"

    def is_loader_installed(self, mc_version: str) -> bool:
        for candidate in self.versions_dir.glob(f"fabric-loader-*-{mc_version}"):
            if (candidate / f"{candidate.name}.json").exists():
                return True
        return False

    def install_loader(self, mc_version: str, force: bool = False) -> None:
        cmd = ["fabric-installer", "client", "-mcversion", mc_version, "-dir", str(self.minecraft_dir)]
        if force:
            cmd.append("-noprofile")
        subprocess.run(cmd, check=True)