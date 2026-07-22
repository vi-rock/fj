from config import settings
from observability.logging import configure_logging


def bootstrap() -> None:
    configure_logging(
        level=settings.logging.level,
        json_logs=settings.logging.is_json,
    )
