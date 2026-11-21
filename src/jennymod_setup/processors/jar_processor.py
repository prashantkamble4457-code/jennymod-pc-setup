"""Processor: verify downloaded JennyMod jars against known SHA-256."""
from __future__ import annotations

import hashlib
from pathlib import Path

from ..models.artifact import Artifact
from ..models.job import InstallJob


def verify_artifact(path: Path, artifact: Artifact) -> bool:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().lower() == artifact.sha256.lower()


def verify_all(job: InstallJob, cache_dir: Path) -> InstallJob:
    for art in job.artifacts:
        local = cache_dir / art.name
        if not local.exists():
            continue
        if not verify_artifact(local, art):
            raise RuntimeError(f"checksum mismatch for {art.name}")
    return job