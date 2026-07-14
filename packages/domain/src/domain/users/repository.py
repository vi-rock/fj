from typing import Protocol

from domain.users.entity import User


class UserRepositoryProtocol(Protocol):
    async def get_by_nickname(self, nickname: str) -> User | None: ...
