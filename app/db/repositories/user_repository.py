from app.db.models.user import User
from app.db.base import Session


class UserRepository:
    @staticmethod
    def create_user(user_data):
        user = User(**user_data)
        session = Session()
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def update_user(user, updated_data):
        for key, value in updated_data.items():
            setattr(user, key, value)
        session = Session()
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def delete_user(user):
        session = Session()
        session.delete(user)
        session.commit()
    
    @staticmethod
    def get_user_by_id(user_id):
        session = Session()
        return session.query(User).get(user_id)

    @staticmethod
    def get_all_users():
        session = Session()
        return session.query(User).all()
