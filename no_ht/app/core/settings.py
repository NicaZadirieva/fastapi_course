from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel):
    app_name: str = "Board API"
    debug: bool = False


class DatabaseSettings(BaseModel):
    url: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    app_name: str = "Board API"
    debug: bool = False

    database_url: str = Field(validation_alias="DATABASE_URL")

    @property
    def db(self) -> DatabaseSettings:
        return DatabaseSettings(url=self.database_url)

    @property
    def app(self) -> AppSettings:
        return AppSettings(debug=self.debug, app_name=self.app_name)


def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


SettingsDeps = Annotated[Settings, Depends(get_settings)]
