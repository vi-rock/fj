from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    id: int = Field(..., ge=1, description="Identifier used to get a cached random user")


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
