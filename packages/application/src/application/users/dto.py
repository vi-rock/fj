from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    nickname: str
