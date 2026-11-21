"""Service: resumable downloader for JennyMod artifacts."""
from __future__ import annotations

import urllib.request
from pathlib import Path

from ..models.artifact import Artifact


class Downloader:
    def __init__(self, cache_dir: Path, timeout: int = 30):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout

    def fetch(self, artifact: Artifact) -> Path:
        dest = self.cache_dir / artifact.name
        if dest.exists() and dest.stat().st_size == artifact.size_bytes:
            return dest
        req = urllib.request.Request(artifact.url, headers={"User-Agent": "jennymod-setup/2.4"})
        with urllib.request.urlopen(req, timeout=self.timeout) as resp, dest.open("wb") as out:
            while chunk := resp.read(1 << 16):
                out.write(chunk)
        return dest