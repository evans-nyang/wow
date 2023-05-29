import os
from datetime import datetime, timedelta
from typing import Any, Dict


from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = os.environ.get("SECURITY_KEY")  # Replace with your own secret key
ALGORITHM = "HS256"  # The algorithm to sign the JWT

TOKEN_BLACKLIST = set()  # In-memory token blacklist

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: Dict[str, Any], expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return password_context.hash(password)

def decode_access_token(token: str) -> Any:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = decoded_token.get("user_id")
        return user_id
    except Exception as e:
        print(e)
        return None
    
def revoke_access_token(token: str) -> bool:
    try:
        TOKEN_BLACKLIST.add(token)
        return True
    except Exception as e:
        print(e)
        return False

def is_token_revoked(token: str) -> bool:
    return token in TOKEN_BLACKLIST