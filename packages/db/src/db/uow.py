from types import TracebackType
from typing import Protocol, Self, runtime_checkable

from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.user import UserRepository, UserRepositoryProtocol


@runtime_checkable
class RepositoriesProtocol(Protocol):
    @property
    def users(self) -> UserRepositoryProtocol: ...


class SqlAlchemyRepositories:
    def __init__(self, session: AsyncSession):
        self.users = UserRepository(session)


@runtime_checkable
class UnitOfWorkProtocol(Protocol):
    session: AsyncSession
    repositories: RepositoriesProtocol

    async def __aenter__(self) -> Self: ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...


class SqlAlchemyUnitOfWork:
    def __init__(self, session: AsyncSession, repositories: SqlAlchemyRepositories):
        self.session = session
        self.repositories = repositories

    async def __aenter__(self) -> Self:
        await self.session.begin()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
