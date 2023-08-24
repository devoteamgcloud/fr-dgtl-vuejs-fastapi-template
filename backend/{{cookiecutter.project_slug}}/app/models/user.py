from app.models.base import AppBase, ReadBase, TableBase


class UserBase(AppBase):
    """User Model"""

    first_name: str
    last_name: str
    email: str


class User(UserBase, TableBase, table=True):
    pass


class UserRead(ReadBase, UserBase):
    id: int


class UserReadTopics(ReadBase, UserBase):
    pass


class UserCreate(User, UserBase):
    pass


class UserUpdate(UserBase):
    pass
