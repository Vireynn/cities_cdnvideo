import json
import redis.asyncio as redis
from typing import Dict, Any

class AsyncRedisClient:
    def __init__(
            self,
            host: str,
            port: int,
            password: str,
            db: int = 0,
    ) -> None:
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=db,
            decode_responses=True
        )
        self.hash_prefix = "cities"

    async def add_new_city(
            self,
            city_name: str,
            coordinates: Dict[str, Any]
    ) -> None:
        await self.redis_client.hset(
            name=self.hash_prefix,
            key=city_name,
            value=json.dumps(coordinates),
        )

    async def get_all_cities(self) -> Dict[str, Any]:
        data = await self.redis_client.hgetall(self.hash_prefix)
        result = {city: json.loads(coordinates) for city, coordinates in data.items()}
        return result

    async def get_city(self, city_name: str) -> Dict[str, Any] | None:
        data = await self.redis_client.hget(
            name=self.hash_prefix,
            key=city_name,
        )
        if data:
            return json.loads(data)
        return None

    async def delete_city(self, city_name: str) -> bool:
        if await self.redis_client.hdel(self.hash_prefix, city_name):
            return True

        return False
