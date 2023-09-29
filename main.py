from app.db.base import Base, engine
from app.services.auth_service import AuthService
from app.utils.security import verify_password
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.api.v1 import auth, orders, products, users, reviews

load_dotenv()

# Initialize the app
app = FastAPI()

Base.metadata.create_all(bind=engine)

# OAuth2 authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Dependency injection for authentication
auth_handler = AuthService()

# Endpoints for logged in users
@app.get("/api/v1/users/me")
async def get_current_user(
    access_token: str = Depends(oauth2_scheme),
):
    """Get the current user's information."""

    user = auth_handler.get_current_user(access_token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return user

@app.post("/api/v1/users/me/change-password")
async def change_password(
    current_password: str,
    new_password: str,
    access_token: str = Depends(oauth2_scheme),
):
    """Change the current user's password."""

    user = auth_handler.get_current_user(access_token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    if not verify_password(current_password, user.password):
        return {"message": "Incorrect password"}

    # Hash the new password
    # hashed_password = hash_password(new_password)

    # Update the user's password
    auth_handler.change_password(current_password, new_password, access_token)
    return {"message": "Password changed successfully"}

# Endpoints for every other user before log in
@app.post("/api/v1/auth/register")
async def register(
    username: str,
    email: str,
    password: str,
):
    """Register a new user."""

    user = auth_handler.register_user(username, email, password)

    return {"message": "User created successfully"}

@app.post("/api/v1/auth/login")
async def login(
    username: str,
    password: str,
):
    """Log in the user."""

    return {"access_token": f"{auth_handler.login(username, password)}"}

@app.get("/api/v1/auth/user")
async def get_user(
    access_token: str = Depends(oauth2_scheme),
):
    """Get the user information for the given access token."""

    user = auth_handler.get_current_user(access_token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return user

# Endpoint to log out the user
@app.post("/api/v1/auth/logout")
async def logout(
    access_token: str = Depends(oauth2_scheme),
):
    """Log out the user."""

    auth_handler.logout(access_token)
    return {"message": "Logged out successfully"}

# Include API routes
# app.include_router(auth.router, prefix="/api/v1")
# app.include_router(orders.router, prefix="/api/v1")
# app.include_router(products.router, prefix="/api/v1")
# app.include_router(users.router, prefix="/api/v1")
# app.include_router(reviews.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
