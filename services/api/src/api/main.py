import uvicorn
from config import settings

from api.bootstrap import bootstrap


def main():
    bootstrap()

    uvicorn.run(
        "api.app:app",
        host=settings.server.host,
        port=settings.server.port,
        log_config=None,
        reload=settings.environment == "local",
        log_level=settings.logging.level,
    )


if __name__ == "__main__":
    main()
