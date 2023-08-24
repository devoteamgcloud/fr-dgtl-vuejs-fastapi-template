from typing import Any

from fastapi import APIRouter

from app.api.endpoints import user


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["User"])


@api_router.get("/health", tags=["Health"])
def get_health() -> Any:
    return {"status": "OK"}
