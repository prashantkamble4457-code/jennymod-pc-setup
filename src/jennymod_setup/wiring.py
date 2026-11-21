"""Assemble the default install pipeline for JennyMod."""
from __future__ import annotations

import uuid
from pathlib import Path

from .pipeline import InstallPipeline
from .models.job import InstallJob
from .ingest.fs_probe import probe_minecraft_dir
from .ingest.manifest_reader import load_manifest
from .processors.fabric_bootstrap import ensure_fabric
from .processors.dependency_resolver import resolve_dependencies
from .processors.jar_processor import verify_all
from .drivers.fs_writer import place_artifacts
from .drivers.report_writer import write_report
from .services.downloader import Downloader

MANIFEST = Path(__file__).parent / "data" / "jenny_manifest.json"
CACHE = Path.home() / ".cache" / "jennymod-setup"


def build_default_pipeline(minecraft_dir: str, mc_version: str, dry_run: bool, force: bool) -> InstallPipeline:
    mc = Path(minecraft_dir).expanduser().resolve()
    job = InstallJob(
        job_id=uuid.uuid4().hex[:8],
        minecraft_dir=mc,
        mc_version=mc_version,
        dry_run=dry_run,
        force=force,
    )

    pipe = InstallPipeline()
    pipe.add("probe", probe_minecraft_dir)
    pipe.add("manifest", lambda j: load_manifest(MANIFEST, j))
    pipe.add("fabric", ensure_fabric)
    pipe.add("resolve", resolve_dependencies)
    pipe.add("download", lambda j: _download(j))
    pipe.add("verify", lambda j: verify_all(j, CACHE))
    pipe.add("place", lambda j: place_artifacts(j, CACHE))
    pipe.add("report", lambda j: (write_report(j, j.minecraft_dir / "jennymod-logs"), j)[1])

    def runner() -> int:
        result = pipe.run_job(job)
        return 0 if result.status.value == "done" else 1

    pipe.run = runner  # type: ignore[method-assign]
    return pipe


def _download(job: InstallJob) -> InstallJob:
    if job.dry_run:
        return job
    dl = Downloader(CACHE)
    for art in job.artifacts:
        dl.fetch(art)
    return job