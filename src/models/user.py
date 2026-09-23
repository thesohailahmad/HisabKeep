
from sqlalchemy import Column,Integer,String , TIMESTAMP , func
from src.database.base import Base

class UserModel(Base):
    __tablename__ = "user_registration"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(100) , nullable=False)
    username = Column(String(100) , nullable=False)
    hash_password = Column(String(100) , nullable=False)
    email = Column(String(120) , nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )