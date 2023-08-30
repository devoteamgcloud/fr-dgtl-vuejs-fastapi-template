from datetime import datetime
from app.models.base import DateTimeModelMixin
from pydantic import BaseModel


class UserBase(BaseModel):
    """User Model"""

    first_name: str
    last_name: str
    email: str


class UserRead(UserBase, DateTimeModelMixin[datetime]):
    pass


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
