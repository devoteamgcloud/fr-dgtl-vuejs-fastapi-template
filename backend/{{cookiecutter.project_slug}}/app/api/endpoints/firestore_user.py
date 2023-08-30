from app.api.deps import raise_400, raise_404, raise_500
from app.models.user import UserCreate, UserUpdate
from fastapi import APIRouter, Depends, status

from app.core.cloud_logging import log

from app import crud
from app.models.base import Page
from app.models.user import UserRead

router = APIRouter()

USER_COLLECTION = "Users"


@router.get(
    "",
    response_model=Page[UserRead],
    status_code=status.HTTP_200_OK,
)
def get_users() -> Page[UserRead]:
    users = crud.firestore.get_all_documents(USER_COLLECTION)
    return {"items": users, "total": len(users)}


@router.get(
    "/{id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
)
def get_user(user_id: str) -> UserRead:
    user = crud.firestore.get_document(USER_COLLECTION, user_id)
    if not user:
        raise_404()
    return user


@router.post(
    "",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
)
def add_user(userData: UserCreate) -> UserCreate:
    update_time, doc_ref = crud.firestore.add_document(
        USER_COLLECTION,
        dict(userData),
    )
    user = doc_ref.get().to_dict()
    return user


@router.put("/{id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_user)])
def update_user(user_id: str, userData: UserUpdate) -> UserRead:
    crud.firestore.update_document(USER_COLLECTION, user_id, dict(userData))
    return dict(userData)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_user)],
)
def delete_user(user_id: str) -> str:
    return crud.firestore.delete_document(USER_COLLECTION, user_id)
