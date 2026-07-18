from pydantic import BaseModel, Field


class UserExistsRequest(BaseModel):
    nickname: str = Field(..., min_length=1, max_length=32)


class UserExistsResponse(BaseModel):
    nickname: str
    exists: bool
