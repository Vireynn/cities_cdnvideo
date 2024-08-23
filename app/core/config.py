from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.settings.app import AppConfig
from app.core.settings.redis import RedisConfig

class Settings(BaseSettings):
    app: AppConfig = AppConfig()
    redis: RedisConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="_",
        extra="allow"
    )


settings = Settings()
