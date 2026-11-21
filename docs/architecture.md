# Architecture

JennyMod Installer For PC is a Python pipeline/worker tool.

```
src/jennymod_setup/
  ingest/       - probe .minecraft, load manifest
  processors/   - fabric bootstrap, dependency resolve, jar verify
  drivers/      - fs writer, report writer
  services/     - downloader, fabric, profile patcher
  models/       - InstallJob, Artifact
  wiring.py     - assembles the default pipeline
```

Each stage is a pure `InstallJob -> InstallJob` function. The pipeline
short-circuits on `FAILED`/`ABORTED`. Output drivers are the only side-effecting
stages (fs_writer, report_writer).