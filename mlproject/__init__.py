"""MLProject package initialization."""

__version__ = "0.2.0"

# Optional: re-export CLI so people can run programmatically
from .cli import cli

__all__ = ["cli", "__version__"]