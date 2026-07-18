from dataclasses import dataclass

from db.uow import UnitOfWorkProtocol


@dataclass(frozen=True)
class CheckUserExistsQuery:
    nickname: str


@dataclass(frozen=True)
class CheckUserExistsResult:
    nickname: str
    exists: bool


class CheckUserExistsUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self._uow: UnitOfWorkProtocol = uow

    async def execute(self, query: CheckUserExistsQuery) -> CheckUserExistsResult:
        async with self._uow as uow:
            exists: bool = await uow.repositories.users.get_by_nickname(query.nickname) is not None
            return CheckUserExistsResult(nickname=query.nickname, exists=exists)
