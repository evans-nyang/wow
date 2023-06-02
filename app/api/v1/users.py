from fastapi import APIRouter

from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/users")
def get_users():
    users = user_service.get_all_users()
    return {"users": users}


@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user:
        return user
    return {"error": "User not found"}


@router.post("/users")
def create_user(user_data: dict):
    user = user_service.create_user(user_data)
    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_data: dict):
    user = user_service.update_user(user_id, updated_data)
    if user:
        return user
    return {"error": "User not found"}


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    user_service.delete_user(user_id)
    return {"message": "User deleted"}
