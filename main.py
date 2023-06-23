import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.db.base import Base
from app.api.v1 import auth, orders, products, users, reviews
from app.services.user_service import UserService
from app.db.repositories.user_repository import UserRepository
from app.utils.security import create_access_token, verify_password

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Security and authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository()
    return UserService(user_repository)

def authenticate_user(
    username: str,
    password: str,
    user_service: UserService = Depends(get_user_service),
):
    db = SessionLocal()
    user = user_service.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_jwt_token(user_id: int):
    encoded_jwt = jwt.encode({"user_id": user_id}, "secret_key", algorithm="HS256")
    return encoded_jwt

def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends(get_user_service),
    db=Depends(get_db),
):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        user = user_service.get_user_by_id(db, payload["user_id"])
        return user
    except JWTError:
        return None

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str

@app.get("/")
async def root():
    return {"message": "Welcome to Weed on Wheels API!"}

@app.post("/api/v1/auth/login")
async def login(username: str, password: str, db=Depends(get_db)):
    user_service = get_user_service(db)
    user = authenticate_user(username=username, password=password, user_service=user_service)
    if not user:
        return {"message": "Invalid credentials"}
    token = create_jwt_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/v1/users/me", response_model=UserResponse)
async def get_current_user_info(current_user=Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return UserResponse(
        user_id=current_user.id,
        username=current_user.username,
        email=current_user.email,
    )

# Include API routes
app.include_router(auth.router, prefix="/api/v1")
app.include_router(orders.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(reviews.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
