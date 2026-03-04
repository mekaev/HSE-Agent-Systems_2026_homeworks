from functools import lru_cache
from pathlib import Path
from uuid import uuid4

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")

    api_key: str = Field(validation_alias="GIGACHAT_API_KEY")
    giga_auth_url: str = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    giga_ruid: str = Field(
        default_factory=lambda: str(uuid4()), validation_alias="GIGACHAT_RQUID"
    )
    ssl_verify: bool | str = Field(default=True, validation_alias="GIGACHAT_SSL_VERIFY")

    polza_ai_api_key: str
    openai_api_key: str = Field(default="", validation_alias="OPENAI_API_KEY")
    github_token: str = Field(default="", validation_alias="GITHUB_TOKEN")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
