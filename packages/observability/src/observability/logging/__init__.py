import structlog

from observability.logging.config import configure_logging


def get_logger(name: str | None = None):
    return structlog.get_logger(name)


__all__ = [
    "get_logger",
    "configure_logging",
]
