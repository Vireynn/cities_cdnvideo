from app.cache.redis_client import AsyncRedisClient
from app.core.config import settings

async def get_redis_client():
    yield AsyncRedisClient(
        host=settings.redis.host,
        port=settings.redis.port,
        password=settings.redis.password,
        db=settings.redis.db,
    )
