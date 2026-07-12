from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import session_factory
from db.uow import SqlAlchemyRepositories, SqlAlchemyUnitOfWork, UnitOfWorkProtocol


async def _session() -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        yield session


class DBProvider(Provider):
    scope = Scope.REQUEST

    session = provide(staticmethod(_session), provides=AsyncSession)
    repositories = provide(SqlAlchemyRepositories)
    unit_of_work = provide(SqlAlchemyUnitOfWork, provides=UnitOfWorkProtocol)
