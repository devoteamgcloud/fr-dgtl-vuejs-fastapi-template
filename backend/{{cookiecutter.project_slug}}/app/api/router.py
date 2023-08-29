from typing import Any

from fastapi import APIRouter

from app.api.endpoints import user
from app.api.endpoints import firestore_user


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["User"])
api_router.include_router(
    firestore_user.router, prefix="/firestore_users", tags=["Firestore User"]
)


@api_router.get("/health", tags=["Health"])
def get_health() -> Any:
    return {"status": "OK"}
