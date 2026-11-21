"""Processor: resolve and order JennyMod dependency graph."""
from __future__ import annotations

from ..models.artifact import Artifact
from ..models.job import InstallJob


def resolve_dependencies(job: InstallJob) -> InstallJob:
    # Required artifacts first, then optional; stable by name.
    job.artifacts.sort(key=lambda a: (not a.required, a.name))
    return job


def missing_required(job: InstallJob) -> list[Artifact]:
    return [a for a in job.artifacts if a.required and a.size_bytes == 0]