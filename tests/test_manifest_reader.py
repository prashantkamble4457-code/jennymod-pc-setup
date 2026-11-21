from pathlib import Path

import pytest

from jennymod_setup.ingest.manifest_reader import load_manifest
from jennymod_setup.models.job import InstallJob


def test_load_manifest_happy(tmp_path: Path):
    manifest = Path(__file__).parent / "fixtures" / "manifest.json"
    job = InstallJob(job_id="t1", minecraft_dir=tmp_path, mc_version="1.20.1")
    job = load_manifest(manifest, job)
    assert len(job.artifacts) >= 1
    assert all(a.sha256 for a in job.artifacts)


def test_unsupported_version_raises(tmp_path: Path):
    manifest = Path(__file__).parent / "fixtures" / "manifest.json"
    job = InstallJob(job_id="t2", minecraft_dir=tmp_path, mc_version="1.7.10")
    with pytest.raises(LookupError):
        load_manifest(manifest, job)