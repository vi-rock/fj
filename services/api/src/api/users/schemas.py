from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    nickname: str = Field(..., min_length=1, max_length=32)


class UserResponse(BaseModel):
    nickname: str
    exists: bool
