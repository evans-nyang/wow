from app.db.models.user import User
from app.db.base import SessionLocal


class UserRepository:
    @staticmethod
    def create_user(username, email, password):
        user = User(username=username, email=email, password=password)
        session = SessionLocal()
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def update_user(username, email):
        user = User(username=username, email=email)
        session = SessionLocal()
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def delete_user(user):
        session = SessionLocal()
        session.delete(user)
        session.commit()
    
    @staticmethod
    def get_user_by_id(user_id):
        session = SessionLocal()
        return session.query(User).get(user_id)

    @staticmethod
    def get_all_users(db):
        session = SessionLocal()
        return session.query(User).all()
    
    @staticmethod
    def get_user_by_username(db, username):
        session = SessionLocal()
        return session.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_email(db, email):
        session = SessionLocal()
        return session.query(User).filter(User.email == email).first()
