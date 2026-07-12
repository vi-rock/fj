from typing import Protocol, runtime_checkable

from db.models.user import User
from db.repositories.base import RepositoryProtocol, SqlAlchemyRepository
from sqlalchemy import select


@runtime_checkable
class UserRepositoryProtocol(RepositoryProtocol, Protocol):
    async def get_by_nickname(self, nickname: str) -> User | None: ...


class UserRepository(SqlAlchemyRepository):
    async def get_by_nickname(self, nickname: str) -> User | None:
        statement = select(User).where(User.nickname == nickname)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()
