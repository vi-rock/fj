from domain.users.entity import User

from db.models.user import UserORM


class UserMapper:
    @staticmethod
    def to_domain(
        model: UserORM,
    ) -> User:
        return User(
            id=model.id,
            nickname=model.nickname,
        )

    @staticmethod
    def to_orm(
        entity: User,
    ) -> UserORM:
        return UserORM(
            id=entity.id,
            nickname=entity.nickname,
        )
