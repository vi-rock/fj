from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    user: str = Field(default="fj", validation_alias="POSTGRES_USER")
    password: str = Field(default="fj", validation_alias="POSTGRES_PASSWORD")
    host: str = Field(default="localhost", validation_alias="POSTGRES_HOST")
    port: int = Field(default=5432, validation_alias="POSTGRES_PORT")
    database: str = Field(default="fj", validation_alias="POSTGRES_DB")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = "local"
    database: DatabaseConfig = DatabaseConfig()


settings = Settings()
