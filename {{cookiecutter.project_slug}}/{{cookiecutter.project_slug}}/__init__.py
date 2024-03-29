"""Top-level package for {{ cookiecutter.project_name }}."""

from .cli import cli
from .version import __version__, __timestamp__, __author__, __email__

__all__ = ["cli", "__version__", "__timestamp__", "__author__", "__email__"]

