from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session

from app import crud
from app.api.deps import get_iap_user, get_session, parse_query_filter_params
from app.core.cloud_logging import log
from app.core.config import settings
from app.models.base import Page, QueryFilter
from app.models.user import User, UserCreate, UserRead

router = APIRouter()


@router.get(
    "",
    response_model=Page[UserRead],
    dependencies=[Depends(get_iap_user)],
)
def read_user(
    *,
    db: Session = Depends(get_session),
    skip: Optional[int] = Query(0, ge=0),
    limit: Optional[int] = Query(None, ge=1, le=settings.MAX_PAGE_SIZE),
    sort: Optional[str] = None,
    filters: List[QueryFilter] = Depends(parse_query_filter_params),
    is_desc: bool = False,
) -> Page[User]:
    """
    Retrieve user.
    """
    users = crud.users.get_multi(
        db, skip=skip, limit=limit, sort=sort, is_desc=is_desc, filters=filters
    )
    return users


@router.post(
    "",
    response_model=UserRead,
)
def create_user(
    *,
    db: Session = Depends(get_session),
    user_in: UserCreate,
) -> User:
    """
    Create new user.
    """
    try:
        user = crud.users.create(db=db, obj_in=user_in)
    except Exception as e:
        log.exception(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not create user"
        )
    return user
