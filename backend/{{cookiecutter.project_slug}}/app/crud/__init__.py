from app.crud.base import CRUDBase
from app.models.user import User, UserCreate, UserUpdate

users = CRUDBase[User, UserCreate, UserUpdate](User)