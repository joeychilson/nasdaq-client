from importlib.metadata import version

from .client import NasdaqError, NasdaqClient

__all__ = ["NasdaqError", "NasdaqClient"]
__version__ = version("nasdaq-client")
