from structlog.contextvars import bind_contextvars, clear_contextvars, unbind_contextvars


def clear() -> None:
    clear_contextvars()


def bind(**kwargs: object) -> None:
    bind_contextvars(**kwargs)


def unbind(*keys: str) -> None:
    unbind_contextvars(*keys)
