from app.cache.redis_client import AsyncRedisClient

async def check_city_name_is_exist(
        city_name: str,
        redis: AsyncRedisClient
):
    if await redis.redis_client.hexists(
        name=redis.hash_prefix,
        key=city_name
    ):
        return True

    return False
