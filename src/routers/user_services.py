from src.models.user import UserModel
from src.schemas.user import UserCreate , UserResponse , UserLogin , Token
from fastapi import APIRouter , Depends , status , HTTPException , Query
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.core.security import hash_password , verify_password , create_access_token

router = APIRouter(prefix="/user" , tags=["User"])

@router.post("/register/",
            response_model=UserResponse,
            status_code= status.HTTP_201_CREATED,
)

def register_user(data:UserCreate , db : Session = Depends(get_db)):

    existing_user = db.query(UserModel).filter(
        UserModel.username == data.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    existing_email = db.query(UserModel).filter(
        UserModel.email == data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = UserModel(
        name=data.name,
        username=data.username,
        hash_password=hash_password(data.password),
        email=data.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login/",
            response_model=Token,
            status_code= status.HTTP_200_OK,
)
def login_user(data:UserLogin , db : Session = Depends(get_db)):
    user = db.query(UserModel).filter(
    UserModel.username == data.username
).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or Password"
        )
    if not verify_password(data.password, user.hash_password):
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )
    access_token = create_access_token(
    {"sub": str(user.id)}
)
    return {
    "access_token": access_token,
    "token_type": "bearer"
}
    

    
