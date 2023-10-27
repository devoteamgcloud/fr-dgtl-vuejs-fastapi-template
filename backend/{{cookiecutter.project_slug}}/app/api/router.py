from typing import Any

from fastapi import APIRouter

from app.api.endpoints import firestore_user as user


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["Firestore User"])


@api_router.get("/health", tags=["Health"])
def get_health() -> Any:
    return {"status": "OK"}
