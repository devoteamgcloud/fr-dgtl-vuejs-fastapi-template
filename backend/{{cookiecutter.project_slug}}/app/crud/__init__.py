from app.crud.base import CRUDBase
from app.models.user import User, UserCreate, UserUpdate

from app.crud.firestore import Firestore

users = CRUDBase[User, UserCreate, UserUpdate](User)

firestore = Firestore()
