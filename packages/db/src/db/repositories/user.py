from domain.users.entity import User
from sqlalchemy import select

from db.mappers.user import UserMapper
from db.models.user import UserORM
from db.repositories.base import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository):
    async def get_by_nickname(self, nickname: str) -> User | None:
        statement = select(UserORM).where(UserORM.nickname == nickname)
        result = await self.session.execute(statement)
        model = result.scalar_one_or_none()
        return UserMapper.to_domain(model) if model else None
