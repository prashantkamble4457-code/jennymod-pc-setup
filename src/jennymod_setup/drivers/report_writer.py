"""Output driver: emit a JSON install report next to the minecraft dir."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ..models.job import InstallJob


def write_report(job: InstallJob, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "job_id": job.job_id,
        "mc_version": job.mc_version,
        "status": job.status.value,
        "placed_files": [str(p) for p in job.placed_files],
        "error": job.error,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    path = out_dir / f"jenny-install-{job.job_id}.json"
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return path