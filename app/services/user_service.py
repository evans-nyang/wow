from app.db.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        return self.user_repository.create_user(user_data)

    def update_user(self, user_id, updated_data):
        user = self.get_user_by_id(user_id)
        if user:
            return self.user_repository.update_user(user, updated_data)
        return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.user_repository.delete_user(user)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_username(self, username):
        return self.user_repository.get_user_by_username(username)
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)
