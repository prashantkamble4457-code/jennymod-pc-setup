"""Output driver: place artifacts into .minecraft with atomic writes."""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from ..models.job import InstallJob


def place_artifacts(job: InstallJob, cache_dir: Path) -> InstallJob:
    if job.dry_run:
        return job
    for art in job.artifacts:
        src = cache_dir / art.name
        if not src.exists():
            if art.required:
                raise FileNotFoundError(f"missing required artifact: {art.name}")
            continue
        dest = job.minecraft_dir / art.target_relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and not job.force:
            continue
        with tempfile.NamedTemporaryFile(delete=False, dir=dest.parent) as tmp:
            shutil.copyfileobj(src.open("rb"), tmp)
            tmp_path = Path(tmp.name)
        tmp_path.replace(dest)
        job.placed_files.append(dest)
    return job