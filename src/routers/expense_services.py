from src.models.expense import ExpenseModel
from typing import List
from src.schemas.expenses import CreateExpense , ExpenseResponse , UpdateExpense

from fastapi import APIRouter , Depends , status , HTTPException , Query
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.core.oauth2 import get_current_user

router = APIRouter(prefix="/expenses" , tags=["Expenses"])

@router.post("/add_expense/",
            response_model=ExpenseResponse,
            status_code= status.HTTP_201_CREATED,
)

def create_expense(data : CreateExpense , db : Session = Depends(get_db) , current_user = Depends(get_current_user)):
    new_expense = ExpenseModel(**data.model_dump(), user_id=current_user.id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/View_expense/",
            response_model=List[ExpenseResponse],
            status_code=status.HTTP_200_OK,
)

def view_expense(db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    view = db.query(ExpenseModel).filter(ExpenseModel.user_id == current_user.id).all()
    return view

@router.get("/View_expense/{id}",
            response_model= ExpenseResponse,
            status_code=status.HTTP_200_OK,
)
def view_single_expense( id : int , db : Session = Depends(get_db) , current_user = Depends(get_current_user) ):
    view = db.query(ExpenseModel).filter(ExpenseModel.id == id ,ExpenseModel.user_id == current_user.id).first()
    if view is None:
        raise HTTPException(
            status_code=404,
            detail=f"Expense with {id} id not found",
     )
    return view

@router.put("/Update_expense/{id}",
        response_model= ExpenseResponse,
        status_code=status.HTTP_200_OK,
)

def update_expense(data:UpdateExpense, id : int , db : Session = Depends(get_db) , current_user = Depends(get_current_user)):
    update = db.query(ExpenseModel).filter(ExpenseModel.id == id , ExpenseModel.user_id == current_user.id).first()
    if update is None:
        raise HTTPException(
            status_code=404,
            detail=f"Expense with {id} id not found",
    )
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(update,field,value)

    db.commit()
    db.refresh(update)

    return update

@router.delete("/delete_expense/{id}",
        response_model= ExpenseResponse,
        status_code=status.HTTP_200_OK,
)

def delete_expense(id : int , db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete = db.query(ExpenseModel).filter(ExpenseModel.id == id , ExpenseModel.user_id == current_user.id).first()
    if delete is None:
        raise HTTPException(
            status_code=404,
            detail=f"Expense with {id} id not found",
        )
    response_data = ExpenseResponse.model_validate(delete)
    db.delete(delete)
    db.commit()
    return response_data


    
    