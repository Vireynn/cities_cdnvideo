from typing import Dict, Any

import aiohttp

from app.core.config import settings
from app.core.errors import CityWasNotFound

async def fetch_coordinates(city_name: str) -> Dict[str, Any]:
    url = "https://graphhopper.com/api/1/geocode"
    query = {
        "q": city_name,
        "key": settings.app.api_key
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=query) as response:
            # response = await session.get(url=url, params=query)
            if response.status == 200:
                data = await response.json()
                if city_info := data.get("hits"):
                    lat = city_info[0]["point"]["lat"]
                    lng = city_info[0]["point"]["lng"]

                    return {
                        "lat": lat,
                        "lng": lng,
                    }
            raise CityWasNotFound(
                f"No city with the name {city_name} was found."
            )
