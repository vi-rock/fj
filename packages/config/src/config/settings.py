from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthConfig(BaseModel):
    private_key: str = Field(default="fj", validation_alias="PRIVATE_KEY")
    public_key: str = Field(default="fj", validation_alias="PUBLIC_KEY")
    access_token_expire_minutes: int = Field(
        default=30, validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    invite_enabled: bool = Field(default=True, validation_alias="INVITE_ENABLED")
    registration_enabled: bool = Field(default=False, validation_alias="REGISTRATION_ENABLED")
    oauth2_enabled: bool = Field(default=False, validation_alias="OAUTH2_ENABLED")


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
    auth: AuthConfig = AuthConfig()


settings = Settings()
