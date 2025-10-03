"""MLProject package initialization."""

__version__ = "0.1.4"

# Optional: re-export CLI so people can run programmatically
from .cli import cli

__all__ = ["cli", "__version__"]