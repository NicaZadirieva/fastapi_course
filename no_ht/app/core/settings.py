from typing import Annotated
from urllib.parse import urlparse
from fastapi import Depends, Request
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel):
    name: str = "Board API"
    debug: bool = False


class DatabaseSettings(BaseModel):
    url: str
    url_sync: str


class AuthSettings(BaseModel):
    jwt_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    app_name: str = "Board API"
    debug: bool = False

    database_url: str
    database_url_sync: str

    jwt_secret: str

    @property
    def db(self) -> DatabaseSettings:
        return DatabaseSettings(url=self.database_url, url_sync=self.database_url_sync)

    @property
    def app(self) -> AppSettings:
        return AppSettings(debug=self.debug, name=self.app_name)

    @property
    def auth(self) -> AuthSettings:
        return AuthSettings(jwt_secret=self.jwt_secret)

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value):
        parsed = urlparse(value)
        if parsed.scheme not in {"postgresql", "postgresql+asyncpg"}:
            raise ValueError(
                "Database_url scheme must be postgresql or postgresql+asyncpg"
            )
        if not parsed.hostname:
            raise ValueError("Database_url must include hostname")

        dbname = (parsed.path or "").lstrip("/")
        if not dbname:
            raise ValueError("Database_url must include database")

        if parsed.port is not None and not (1 <= parsed.port <= 65535):
            raise ValueError("Database_url port must be 1...65535")

        return value


def get_settings(request: Request) -> Settings:
    return request.app.state.settings


SettingsDeps = Annotated[Settings, Depends(get_settings)]
