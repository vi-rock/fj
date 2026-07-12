from db.di import DBProvider
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from api.provider import APIProvider

container = make_async_container(
    DBProvider(),
    APIProvider(),
    FastapiProvider(),
)
