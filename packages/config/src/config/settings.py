from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CORSConfig(BaseModel):
    allowed_origins: list[str] = []
    allow_credentials: bool = True


class ServerConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class LoggingConfig(BaseModel):
    level: str = "INFO"
    is_json: bool = False


class DatabaseConfig(BaseModel):
    user: str = "fj"
    password: str = "fj"
    host: str = "localhost"
    port: int = 5432
    database: str = "fj"


class AuthConfig(BaseModel):
    private_key: str = "fj"
    public_key: str = "fj"
    access_token_expire_minutes: int = 30
    invite_enabled: bool = True
    registration_enabled: bool = False
    oauth2_enabled: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        extra="ignore",
    )

    environment: str = "local"

    cors: CORSConfig = Field(default_factory=CORSConfig)
    server: ServerConfig = Field(default_factory=ServerConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    auth: AuthConfig = Field(default_factory=AuthConfig)


settings = Settings()
