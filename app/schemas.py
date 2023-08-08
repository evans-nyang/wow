from pydantic import BaseModel

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
