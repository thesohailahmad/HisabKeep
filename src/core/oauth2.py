from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import PyJWTError
from sqlalchemy.orm import Session

from src.database.db import settings
from src.database.session import get_db
from src.models.user import UserModel


oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/login/')
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def get_current_user(token: str = Depends(oauth2_schema) , db : Session = Depends(get_db)):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
    except PyJWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    user_id  = payload.get('sub')
    
    if user_id is None:
         raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid Token credentials"
            )
    # user_id_int = int(user_id)
    user = db.query(UserModel).filter(
       UserModel.id == int(user_id)
    ).first()

    if user is None:
             raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User Not found"
                )

    return user




