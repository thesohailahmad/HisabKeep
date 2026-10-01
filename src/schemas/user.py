from pydantic import BaseModel , ConfigDict , Field , EmailStr
from datetime import datetime
from typing import Annotated

# UserBase class defines the base schema for user data, including name, username, and email fields with validation constraints.
class UserBase(BaseModel):
    name : Annotated[str ,Field(...,max_length=150 , title= "Name",description= "Name of User")]
    username : Annotated[str ,Field(...,max_length=150 , title= "Username",description= "Username for login")]
    email : Annotated[EmailStr , Field(...,max_length=150,title="Email" , description="Email of user")]

#UserCreate class extends UserBase and adds a password field with validation constraints for creating a new user.
class UserCreate(UserBase):
    password : Annotated[str , Field(...,min_length=8 , max_length=16 , title="Password" , description="Password must be at least 8 characters long")]

#UserResponse class extends UserBase and adds id and created_at fields for returning user data in responses.
class UserResponse(UserBase):
    id : int
    created_at : datetime
 # model_config attribute specifies that the model should be populated from ORM(Object Relational Mapping) objects, 
 # allowing for seamless integration with database models.
    model_config = ConfigDict(from_attributes=True)

#UserLogin class defines the schema for user login data, including username and password fields.
class UserLogin(BaseModel):
    username : str
    password : str

#Token class defines the schema for authentication tokens, including access_token and token_type fields.
class Token(BaseModel):
    access_token: str
    token_type: str