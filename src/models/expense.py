from sqlalchemy import Column,Integer,String , TIMESTAMP , func
from src.database.base import Base

class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(100) , nullable=False)
    category = Column(String(100) , nullable=True)
    discription = Column(String(300) , nullable=True)
    amount = Column(Integer ,  nullable=False )
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )