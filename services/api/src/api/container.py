from application.users.provider import UserApplicationProvider
from db.provider import DBProvider
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

container = make_async_container(
    DBProvider(),
    # application providers
    UserApplicationProvider(),
    # framework provider
    FastapiProvider(),
)
