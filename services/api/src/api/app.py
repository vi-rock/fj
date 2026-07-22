from contextlib import asynccontextmanager

from application.users.queries.check_user_exists import CheckUserExistsQuery, CheckUserExistsUseCase
from dishka.integrations.fastapi import FromDishka, inject, setup_dishka
from fastapi import FastAPI
from observability.logging import get_logger

from api.container import container
from api.users.schemas import UserExistsRequest, UserExistsResponse

logger = get_logger(__name__)


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
    payload: UserExistsRequest,
    use_case: FromDishka[CheckUserExistsUseCase],
) -> UserExistsResponse:
    result = await use_case.execute(
        query=CheckUserExistsQuery(
            nickname=payload.nickname,
        ),
    )

    return UserExistsResponse(
        nickname=result.nickname,
        exists=result.exists,
    )
