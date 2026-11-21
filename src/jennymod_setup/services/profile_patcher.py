"""Service: patch launcher_profiles.json to expose the JennyMod profile."""
from __future__ import annotations

import json
import uuid
from pathlib import Path


PROFILE_NAME = "JennyMod (Fabric)"


def ensure_profile(minecraft_dir: Path, mc_version: str) -> bool:
    launcher = minecraft_dir / "launcher_profiles.json"
    if not launcher.exists():
        return False
    data = json.loads(launcher.read_text(encoding="utf-8"))
    profiles = data.setdefault("profiles", {})
    if any(p.get("name") == PROFILE_NAME for p in profiles.values()):
        return False
    key = uuid.uuid4().hex[:16]
    profiles[key] = {
        "name": PROFILE_NAME,
        "lastVersionId": f"fabric-loader-0.15.7-{mc_version}",
        "type": "custom",
    }
    launcher.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return True