"""Regenerate data/jenny_manifest.json from the CDN index."""
import json
import urllib.request
from pathlib import Path

INDEX = "https://cdn.jennymod.dev/index.json"
OUT = Path(__file__).resolve().parents[1] / "src" / "jennymod_setup" / "data" / "jenny_manifest.json"


def main() -> None:
    with urllib.request.urlopen(INDEX, timeout=20) as resp:
        data = json.load(resp)
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()