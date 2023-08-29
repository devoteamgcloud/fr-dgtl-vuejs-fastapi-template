from fastapi import APIRouter, status

from app import crud
from app.models.base import Page
from app.models.user import UserRead

router = APIRouter()


@router.get(
    "",
    response_model=Page[UserRead],
    status_code=status.HTTP_200_OK,
    tags=["Users"],
)
def get_users() -> Page[UserRead]:
    users = crud.firestore.get_all_documents("Users")
    return {"items": users, "total": len(users)}


@router.get(
    "/{id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    tags=["Users"],
)
def get_user(user_id) -> Page[UserRead]:
    return crud.firestore.get_document("Users", user_id)


# def add_user() -> UserRead:
#     users = crud.firestore.get_("Users")
#     return {"items": users, "total": len(users)}


# def updated_user() -> UserRead:
#     users = crud.firestore.update_document("Users")
#     return {"items": users, "total": len(users)}
