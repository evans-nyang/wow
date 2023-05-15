from sqlalchemy.orm import Session
from app.db.repositories.users import UserRepository
from app.models.user import UserCreate, UserInDB

def get_user_by_email(db: Session, email: str) -> UserInDB:
    user = UserRepository(db).get_user_by_email(email)
    if user:
        return UserInDB(**user.__dict__)

def create_user(db: Session, user: UserCreate) -> UserInDB:
    created_user = UserRepository(db).create_user(**user.dict())
    return UserInDB(**created_user.__dict__)
