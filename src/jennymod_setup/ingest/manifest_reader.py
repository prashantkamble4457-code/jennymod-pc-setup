"""Ingest stage: read the JennyMod manifest shipped with the installer."""
from __future__ import annotations

import json
from pathlib import Path

from ..models.artifact import Artifact
from ..models.job import InstallJob


def load_manifest(manifest_path: Path, job: InstallJob) -> InstallJob:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    version = job.mc_version
    entries = data.get("versions", {}).get(version)
    if not entries:
        raise LookupError(f"no JennyMod build for Minecraft {version}")

    arts: list[Artifact] = []
    for entry in entries["artifacts"]:
        arts.append(
            Artifact(
                name=entry["name"],
                url=entry["url"],
                sha256=entry["sha256"],
                target_relative=Path(entry["target"]),
                size_bytes=entry.get("size", 0),
                required=entry.get("required", True),
            )
        )
    job.artifacts = arts
    return job