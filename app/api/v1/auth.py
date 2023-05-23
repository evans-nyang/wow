from fastapi import APIRouter

from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post("/register")
def register_user(user_data: dict):
    user = auth_service.register_user(user_data)
    return user


@router.post("/login")
def login(username: str, password: str):
    access_token = auth_service.login(username, password)
    if access_token:
        return {"access_token": access_token}
    return {"error": "Invalid username or password"}


@router.post("/logout")
def logout():
    auth_service.logout()
    return {"message": "Logged out successfully"}


@router.get("/user")
def get_current_user():
    user = auth_service.get_current_user()
    if user:
        return user
    return {"error": "User not authenticated"}


@router.put("/change-password")
def change_password(current_password: str, new_password: str):
    result = auth_service.change_password(current_password, new_password)
    if result:
        return {"message": "Password changed successfully"}
    return {"error": "Failed to change password"}
