from dishka import Provider, Scope, provide

from application.users.queries.check_user_exists import CheckUserExistsUseCase


class UserApplicationProvider(Provider):
    scope = Scope.REQUEST

    check_user_exists = provide(
        CheckUserExistsUseCase,
    )
