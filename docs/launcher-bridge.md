# Launcher Bridge (C#)

Optional component that mirrors what `services/profile_patcher.py` does, for
hosts that want a signed native helper instead of running Python.

```
dotnet build src/JennyMod.LauncherBridge/JennyMod.LauncherBridge.csproj -c Release
```

The bridge only edits `launcher_profiles.json`; it does not install jars.
Keep the Python installer as the source of truth for artifact placement.