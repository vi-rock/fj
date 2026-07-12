from db.di import DBProvider
from dishka import Provider, Scope, make_async_container, provide
from dishka.integrations.fastapi import FastapiProvider

from api.users.service import UserService


class APIProvider(Provider):
    scope = Scope.REQUEST

    user_service = provide(UserService)


container = make_async_container(
    DBProvider(),
    APIProvider(),
    FastapiProvider(),
)
