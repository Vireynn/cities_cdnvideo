from pydantic import BaseModel, Field

class CityRequest(BaseModel):
    city_name: str = Field(..., max_length=255)

class CityResponse(CityRequest):
    lat: float
    lng: float
