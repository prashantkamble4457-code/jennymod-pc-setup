from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Artifact:
    """A downloadable JennyMod component (fabric loader, jenny mod jar, deps)."""
    name: str
    url: str
    sha256: str
    target_relative: Path
    size_bytes: int = 0
    required: bool = True