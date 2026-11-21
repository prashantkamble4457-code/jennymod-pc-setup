from __future__ import annotations

import os
from pathlib import Path


def default_minecraft_dir() -> Path:
    if os.name == "nt":
        return Path(os.environ.get("APPDATA", Path.home())) / ".minecraft"
    return Path.home() / ".minecraft"


def is_windows() -> bool:
    return os.name == "nt"