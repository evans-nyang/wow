from sqlalchemy.orm import Session
from app.db.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, name: str, email: str, password: str, phone_number: str) -> User:
        user = User(name=name, email=email, password=password, phone_number=phone_number)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
