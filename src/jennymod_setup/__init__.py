"""JennyMod Installer For PC — bootstrap package."""

__version__ = "2.4.1"
__app_name__ = "JennyMod Installer For PC"

from .pipeline import InstallPipeline

__all__ = ["InstallPipeline", "__version__", "__app_name__"]