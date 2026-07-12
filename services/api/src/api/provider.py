from dishka import Provider, Scope, provide

from api.users.service import UserService


class APIProvider(Provider):
    scope = Scope.REQUEST

    user_service = provide(UserService)
