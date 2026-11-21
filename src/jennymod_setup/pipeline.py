"""Job pipeline: ingest -> process -> emit for JennyMod install jobs."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterable

from .models.job import InstallJob, JobStatus
from .models.artifact import Artifact


Stage = Callable[[InstallJob], InstallJob]


@dataclass
class InstallPipeline:
    stages: list[Stage] = field(default_factory=list)
    on_stage: Callable[[str, InstallJob], None] | None = None

    def add(self, name: str, stage: Stage) -> "InstallPipeline":
        def wrapped(job: InstallJob) -> InstallJob:
            if self.on_stage:
                self.on_stage(name, job)
            return stage(job)
        self.stages.append(wrapped)
        return self

    def run_job(self, job: InstallJob) -> InstallJob:
        job.status = JobStatus.RUNNING
        try:
            for stage in self.stages:
                job = stage(job)
                if job.status in (JobStatus.FAILED, JobStatus.ABORTED):
                    return job
            job.status = JobStatus.DONE
        except Exception as exc:  # noqa: BLE001
            job.status = JobStatus.FAILED
            job.error = str(exc)
        return job

    def run(self) -> int:
        raise NotImplementedError("wired pipeline runs via wiring.build_default_pipeline")