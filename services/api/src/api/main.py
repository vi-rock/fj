from collections import OrderedDict
from random import choice, randint

from fastapi import FastAPI

from api.users.schemas import UserRequest, UserResponse

app = FastAPI(title="FJ API")


_USER_CACHE_LIMIT = 128
_user_cache: OrderedDict[int, UserResponse] = OrderedDict()


def _build_random_user(user_id: int) -> UserResponse:
    first_names = ["Alex", "Mira", "Sam", "Nina", "Oleg", "Ira"]
    last_names = ["Stone", "River", "Fox", "Lane", "Vale", "Brooks"]

    name = f"{choice(first_names)} {choice(last_names)}"
    email = f"user{user_id}-{randint(1000, 9999)}@example.com"

    return UserResponse(
        id=user_id,
        name=name,
        email=email,
        age=randint(18, 70),
    )


def get_or_create_user(user_id: int) -> UserResponse:
    cached_user = _user_cache.get(user_id)
    if cached_user is not None:
        _user_cache.move_to_end(user_id)
        return cached_user

    user = _build_random_user(user_id)
    _user_cache[user_id] = user
    if len(_user_cache) > _USER_CACHE_LIMIT:
        _user_cache.popitem(last=False)

    return user


@app.get("/hello")
async def root():
    return {"message": "hello FJ"}


@app.post("/user/")
async def get_user(user_id: UserRequest) -> UserResponse:
    return get_or_create_user(user_id.id)
