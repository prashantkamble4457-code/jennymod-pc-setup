"""Ingest stage: validate .minecraft layout before touching anything."""
from __future__ import annotations

from pathlib import Path

from ..models.job import InstallJob


REQUIRED_DIRS = ("mods", "config", "versions")


def probe_minecraft_dir(job: InstallJob) -> InstallJob:
    root = job.minecraft_dir
    if not root.is_dir():
        raise FileNotFoundError(f"minecraft dir not found: {root}")
    missing = [d for d in REQUIRED_DIRS if not (root / d).is_dir()]
    if missing:
        raise RuntimeError(f"not a valid minecraft install, missing: {', '.join(missing)}")
    return job