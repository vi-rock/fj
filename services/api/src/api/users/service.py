from db.uow import UnitOfWorkProtocol


class UserService:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    async def user_exists(self, nickname: str) -> bool:
        async with self.uow:
            user = await self.uow.repositories.users.get_by_nickname(nickname)
        return user is not None
