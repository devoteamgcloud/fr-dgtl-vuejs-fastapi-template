from typing import Any

from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/health", tags=["Health"])
def get_health() -> Any:
    return {"status": "OK"}
