from contextlib import asynccontextmanager

from dishka.integrations.fastapi import FromDishka, inject, setup_dishka
from fastapi import FastAPI

from api.container import container
from api.users.schemas import UserRequest, UserResponse
from api.users.service import UserService


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


app = FastAPI(title="FJ API", lifespan=lifespan)

setup_dishka(container, app)


@app.get("/hello")
async def root():
    return {"message": "hello FJ"}


@app.post("/exists")
@inject
async def check_user_exists(
    payload: UserRequest,
    user_service: FromDishka[UserService],
) -> UserResponse:
    exists = await user_service.user_exists(payload.nickname)
    return UserResponse(nickname=payload.nickname, exists=exists)
