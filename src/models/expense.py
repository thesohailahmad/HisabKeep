from sqlalchemy import Column,Integer,String , TIMESTAMP , func , ForeignKey
from src.database.base import Base

#class for expense model
#table to store expense data
#ExpenseModel class inherits from Base class which is imported from base.py file
#ExpenseModel connected user_registration table through user_id foreign key
class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String(100) , nullable=False)
    category = Column(String(100) , nullable=True)
    description = Column(String(300) , nullable=True)
    amount = Column(Integer ,  nullable=False )
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    user_id = Column(Integer , ForeignKey("user_registration.id" , ondelete="CASCADE" ))