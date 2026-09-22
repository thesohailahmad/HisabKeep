from pydantic import BaseModel , ConfigDict
from typing import Optional
from datetime import datetime


class ExpenseBase(BaseModel):

    name : str
    category: str 
    discription : str
    amount : int

class CreateExpense(ExpenseBase):
    pass

class UpdateExpense(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    discription: Optional[str] = None
    amount: Optional[int] = None

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)