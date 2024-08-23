import uvicorn
from fastapi import FastAPI

from app.api.api_v1.routes import cities_router
from app.core.config import settings

app = FastAPI(**settings.app.fastapi_kwargs)
app.include_router(cities_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000)
