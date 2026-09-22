from src.models.expense import ExpenseModel
from typing import List
from src.schemas.expenses import CreateExpense , ExpenseResponse , UpdateExpense

from fastapi import APIRouter , Depends , status , HTTPException , Query
from sqlalchemy.orm import Session
from src.database.session import get_db

router = APIRouter(prefix="/expenses" , tags=["Expenses"])

@router.post("/add_expense/",
            response_model=ExpenseResponse,
            status_code= status.HTTP_201_CREATED,
)

def create_expense(data : CreateExpense , db : Session = Depends(get_db)):
    new_expense = ExpenseModel(**data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/View_expense/",
            response_model=List[ExpenseResponse],
            status_code=status.HTTP_200_OK,
)

def view_expense(db : Session = Depends(get_db)):
    view = db.query(ExpenseModel).all()
    return view

@router.get("/View_expense/{id}",
            response_model= ExpenseResponse,
            status_code=status.HTTP_200_OK,
)
def view_expense( id : int , db : Session = Depends(get_db)):
    view = db.query(ExpenseModel).get(id)
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

def update_expense(data:UpdateExpense, id : int , db : Session = Depends(get_db)):
    update = db.query(ExpenseModel).get(id)
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

def delete_expense(id : int , db : Session = Depends(get_db)):
    delete = db.query(ExpenseModel).get(id)
    if delete is None:
        raise HTTPException(
            status_code=404,
            detail=f"Expense with {id} id not found",
        )
    response_data = ExpenseResponse.model_validate(delete)
    db.delete(delete)
    db.commit()
    return response_data


    
    