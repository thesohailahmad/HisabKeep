from pydantic import BaseModel , ConfigDict , Field
from typing import Optional
from datetime import datetime
from typing import Annotated


class ExpenseBase(BaseModel):

    name : Annotated[str ,Field(...,max_length=150 , title= "Name",description= "Name of Expense")]
    category : Annotated[Optional[str],Field(default=None ,max_length=250 , title="Category" , description="Category of Expense")]
    description : Annotated[Optional[str] , Field( default=None    ,max_length=250 , title="Description" , description="Description of Expense")]
    amount : Annotated[int ,Field(...,gt=0 , title="Amount" , description="Amount of Expense")]

class CreateExpense(ExpenseBase):
    pass

class UpdateExpense(BaseModel):
    name: Annotated[Optional[str] ,Field(max_length=150 , title= "Name",description= "Name of Expense")] = None
    category:  Annotated[Optional[str],Field(max_length=250 , title="Category" , description="Category of Expense")] = None
    description: Annotated[Optional[str], Field(max_length=250 , title="Description" , description="Description of Expense")] = None
    amount: Annotated[Optional[int] , Field(gt=0 ,title="Amount" , description="Amount of Expense")] = None

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)