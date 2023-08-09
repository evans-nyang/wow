import os
from datetime import datetime, timedelta
from typing import Any, Dict

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from starlette.responses import Response

SECRET_KEY = os.environ.get("SECURITY_KEY")  # Replace with your own secret key
ALGORITHM = "HS256"  # The algorithm to sign the JWT

TOKEN_BLACKLIST = set()  # In-memory token blacklist

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
access_token_expiry = timedelta(minutes=30)

def create_access_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + access_token_expiry
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain_password: str, hashed_password: str, session=None) -> bool:
    if session is None:
        return password_context.verify(plain_password, hashed_password)
    else:
        return password_context.verify(plain_password, hashed_password, scheme="bcrypt", salt=session)

def hash_password(password: str) -> str:
    return password_context.hash(password)

def decode_access_token(token: str) -> Any:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token.get("user_id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail='Invalid token')
    
def revoke_access_token(token: str) -> bool:
    try:
        TOKEN_BLACKLIST.add(token)
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail='Invalid token')

def is_token_revoked(token: str) -> bool:
    return token in TOKEN_BLACKLIST

def set_access_token_cookie(response: Response, access_token: str):
    response.set_cookie(
        key="access_token",
        value=access_token,
        expires=datetime.utcnow() + timedelta(minutes=30),
        httponly=True,
        secure=True,
        samesite="Strict",
    )
