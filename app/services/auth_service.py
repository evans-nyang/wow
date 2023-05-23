from datetime import timedelta
from app.services.user_service import UserService
from app.utils.security import hash_password, verify_password, create_access_token, decode_access_token, revoke_access_token
from app.utils.session import update_user_session, cleanup_user_session
from fastapi import HTTPException, status

class AuthService:
    def __init__(self):
        self.user_service = UserService()

    def register_user(self, user_data: dict):
        # Extract user credentials from user_data
        username = user_data.get("username")
        email = user_data.get("email")
        password = user_data.get("password")

        # Check if the username or email already exists
        if self.user_service.get_user_by_username(username):
            raise ValueError("Username already exists")
        if self.user_service.get_user_by_email(email):
            raise ValueError("Email already exists")

        # Hash the password
        hashed_password = hash_password(password)

        # Create the user
        user_data["password"] = hashed_password  # Update user_data with hashed password
        user = self.user_service.create_user(user_data)
        return user

    def login(self, username: str, password: str) -> str:
        # Get the user by username
        user = self.user_service.get_user_by_username(username)
        if not user:
            return None

        # Verify the password
        if not verify_password(password, user.password):
            return None

        # Generate and return an access token
        access_token = self.generate_access_token(user.id)
        return access_token

    def logout(self, access_token: str):
        # Validate the access token
        user_id = decode_access_token(access_token)
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")

        # Revoke the access token
        revoked = revoke_access_token(access_token)
        if not revoked:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to revoke access token")

        # Update the user session
        update_user_session(user_id, None)

        # Perform any necessary actions for user logout
        cleanup_user_session(user_id)  # Clean up any additional session-related data or resources

        # Return a success message or any other relevant information
        return {"message": "Logged out successfully"}

    def get_current_user(self, access_token: str):
        # Validate the access token
        user_id = decode_access_token(access_token)
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")

        # Retrieve the current user based on the validated user ID
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        # Return the current user information
        return user

    def change_password(self, current_password: str, new_password: str, access_token: str) -> bool:
        # Validate the access token
        user_id = decode_access_token(access_token)
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")

        # Get the current authenticated user
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        # Verify the current password
        if not verify_password(current_password, user.password):
            return False

        # Hash the new password
        hashed_password = hash_password(new_password)

        # Update the user's password
        self.user_service.update_user(user.id, {"password": hashed_password})
        return True

    def generate_access_token(self, user_id: int) -> str:
        # Generate an access token for the user using a token library or JWT
        access_token_expires = timedelta(minutes=30)  # Define the token expiration time
        access_token = create_access_token({"user_id": user_id}, access_token_expires)
        return access_token
