from typing import Protocol, runtime_checkable

from sqlalchemy.ext.asyncio import AsyncSession


@runtime_checkable
class RepositoryProtocol(Protocol):
    session: AsyncSession


class SqlAlchemyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
