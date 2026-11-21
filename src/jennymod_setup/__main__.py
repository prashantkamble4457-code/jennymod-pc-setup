"""CLI entrypoint for jennymod-pc-setup."""
import argparse
import sys

from .pipeline import InstallPipeline
from .wiring import build_default_pipeline


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="jennymod-setup")
    parser.add_argument("--minecraft-dir", required=True, help="Path to .minecraft folder")
    parser.add_argument("--mc-version", default="1.20.1", help="Target Minecraft version")
    parser.add_argument("--dry-run", action="store_true", help="Plan only, no writes")
    parser.add_argument("--force", action="store_true", help="Overwrite existing JennyMod files")
    args = parser.parse_args(argv)

    pipeline: InstallPipeline = build_default_pipeline(
        minecraft_dir=args.minecraft_dir,
        mc_version=args.mc_version,
        dry_run=args.dry_run,
        force=args.force,
    )
    return pipeline.run()


if __name__ == "__main__":
    sys.exit(main())