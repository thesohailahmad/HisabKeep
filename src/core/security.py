from pwdlib import PasswordHash
from src.database.db import settings
import jwt
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()

def hash_password(password : str) -> str:
    return password_hash.hash(password)


def verify_password(password : str , hash_password : str) -> bool:
    return password_hash.verify(password,hash_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
       algorithm=settings.ALGORITHM
       )

    return encoded_jwt