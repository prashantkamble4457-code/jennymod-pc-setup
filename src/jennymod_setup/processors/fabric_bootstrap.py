"""Processor: ensure Fabric Loader is present for the target MC version."""
from __future__ import annotations

from ..models.job import InstallJob
from ..services.fabric_service import FabricService


def ensure_fabric(job: InstallJob) -> InstallJob:
    svc = FabricService(minecraft_dir=job.minecraft_dir)
    if svc.is_loader_installed(job.mc_version):
        return job
    if job.dry_run:
        return job
    svc.install_loader(job.mc_version, force=job.force)
    return job