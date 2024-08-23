from typing import Dict, List

from fastapi import (
    APIRouter,
    Depends,
    Path,
    HTTPException,
    status,
    Body
)

from app.schemas.city import CityRequest, CityResponse
from app.api.dependencies.cache import get_redis_client
from app.cache.redis_client import AsyncRedisClient
from app.servecies.cities import check_city_name_is_exist
from app.servecies.utils import calculate_distance
from app.servecies import fetch_coordinates

router = APIRouter(prefix="/cities")


@router.get("/city/{city_name}", response_model=CityResponse, name="cities:get-city-by-name")
async def get_city_by_name(
        city_name: str = Path(..., max_length=255),
        redis_client: AsyncRedisClient = Depends(get_redis_client),
) -> CityResponse:
    if not (data := await redis_client.get_city(city_name)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"A city with the name {city_name} was not found"
        )
    return CityResponse(city_name=city_name, **data)


@router.get("/", name="cities:get-all-cities")
async def get_all_cities(
        redis_client: AsyncRedisClient = Depends(get_redis_client)
):
    return await redis_client.get_all_cities()


@router.post("/city/", response_model=CityResponse, name="cities:add-new-city")
async def add_new_city(
        city: CityRequest = Body(..., embed=True),
        redis_client: AsyncRedisClient = Depends(get_redis_client)
):
    if await check_city_name_is_exist(city.city_name, redis_client):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A city with the name {city.city_name} is already exist."
        )

    data = await fetch_coordinates(city.city_name)
    await redis_client.add_new_city(city.city_name, data)
    data.update(city.model_dump())

    return CityResponse(**data)


@router.get("/nearest", name="cities:get-two-nearest-cities")
async def get_nearest_cities(
        lat: float,
        lng: float,
        redis_client: AsyncRedisClient = Depends(get_redis_client)
):
    if not (cities := await redis_client.get_all_cities()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No cities in storage"
        )
    distances = []
    for city_name, coordinates in cities.items():
        city_lat = coordinates.get("lat")
        city_lng = coordinates.get("lng")
        distance = calculate_distance(lat, city_lat, lng, city_lng)
        distances.append((city_name, distance))

    distances.sort(key=lambda x: x[1])
    nearest = distances[:2]
    return nearest


@router.delete("/city/{city_name}", name="cities:delete-city-by-name")
async def delete_city_by_name(
        city_name: str = Path(..., max_length=255),
        redis_client: AsyncRedisClient = Depends(get_redis_client)
) -> Dict[str, str]:
    if not await redis_client.delete_city(city_name):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"A city with the name {city_name} was not found"
        )
    return {
        "successful": "OK"
    }



