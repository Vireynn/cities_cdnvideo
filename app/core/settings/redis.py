from pydantic_settings import BaseSettings

class RedisConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    db: int
