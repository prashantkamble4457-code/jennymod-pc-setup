# Contributing to jennymod-pc-setup

Thanks for helping improve the JennyMod Installer For PC.

## Dev setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Adding a Minecraft version
1. Add the version + artifacts to `src/jennymod_setup/data/jenny_manifest.json`
   (or run `python scripts/sync_manifest.py`).
2. Add a fixture under `tests/fixtures/` if the version changes artifact layout.
3. Open a PR titled `manifest: add MC <version>`.

## Style
- Python 3.11+, type hints everywhere.
- Pipeline stages must be pure `InstallJob -> InstallJob` functions.
- Side effects belong in `drivers/` or `services/`.

## Reporting bugs
Include the JSON report from `<minecraft_dir>/jennymod-logs/`.