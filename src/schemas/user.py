from pydantic import BaseModel , ConfigDict
from datetime import datetime

class UserBase(BaseModel):

    name : str
    username : str
    email : str

class UserCreate(UserBase):
    password : str


class UserResponse(UserBase):
    id : int
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str