from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    ABORTED = "aborted"


@dataclass
class InstallJob:
    job_id: str
    minecraft_dir: Path
    mc_version: str
    dry_run: bool = False
    force: bool = False
    status: JobStatus = JobStatus.PENDING
    artifacts: list["Artifact"] = field(default_factory=list)
    placed_files: list[Path] = field(default_factory=list)
    error: str | None = None