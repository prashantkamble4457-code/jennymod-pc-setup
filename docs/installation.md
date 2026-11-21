# Installing JennyMod For PC

## Requirements
- Minecraft Java Edition (1.19.2 or 1.20.1)
- Fabric Loader compatible launcher
- Windows 10/11 x64

## Quick start
1. Download `JennyModSetup.exe` from the releases page.
2. Run it. The installer auto-detects `%APPDATA%\.minecraft`.
3. Pick your Minecraft version and click **Install**.
4. Launch the "JennyMod (Fabric)" profile in the official launcher.

## Manual install
```
python -m jennymod_setup --minecraft-dir "%APPDATA%\.minecraft" --mc-version 1.20.1
```

## Troubleshooting
- **"not a valid minecraft install"** — pass `--minecraft-dir` explicitly.
- **checksum mismatch** — clear `~/.cache/jennymod-setup` and retry.
- **mod not loading** — confirm Fabric Loader is installed for the same MC version.