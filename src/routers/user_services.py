from src.models.user import UserModel
from src.schemas.user import UserCreate , UserResponse
from fastapi import APIRouter , Depends , status , HTTPException , Query
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.core.security import hash_password

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
