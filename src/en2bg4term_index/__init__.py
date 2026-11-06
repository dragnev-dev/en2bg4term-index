"""Search buffer index and source adapters for the en2bg technical dictionary."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("en2bg4term-index")
except PackageNotFoundError:
    __version__ = "0.0.0"

# After __version__: ingest.base reads it for the User-Agent.
from en2bg4term_index.contract import Candidate, CheckResult, LinkRecord, Provider, SourceInfo  # noqa: E402
from en2bg4term_index.model import IndexVersionError  # noqa: E402
from en2bg4term_index.providers import Registry, load_providers  # noqa: E402
from en2bg4term_index.release import ReleaseError, download_release  # noqa: E402

__all__ = [
    "Candidate",
    "CheckResult",
    "IndexVersionError",
    "LinkRecord",
    "Provider",
    "Registry",
    "ReleaseError",
    "SourceInfo",
    "download_release",
    "load_providers",
]
