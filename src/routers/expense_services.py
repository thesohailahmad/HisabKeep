from src.models.expense import ExpenseModel
from typing import List
from src.schemas.expenses import CreateExpense , ExpenseResponse , UpdateExpense
from fastapi import APIRouter , Depends , status , HTTPException , Query
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.core.oauth2 import get_current_user

router = APIRouter(prefix="/expenses" , tags=["Expenses"])

#expense management endpoints
#add_expense endpoint takes expense data as input and creates a new expense in the database
@router.post("/add_expense/",
            response_model=ExpenseResponse,
            status_code= status.HTTP_201_CREATED,
)

def create_expense(data : CreateExpense , db : Session = Depends(get_db) , current_user = Depends(get_current_user)):
    new_expense = ExpenseModel(**data.model_dump(), user_id=current_user.id)
    
    if new_expense.amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Amount must be greater than zero"
        )
    if not new_expense.name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Name of expense is required"
        )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# view_expense endpoint retrieves all expenses for the current user from the database
@router.get("/View_expense/",
            response_model=List[ExpenseResponse],
            status_code=status.HTTP_200_OK,
)

# view_expense function retrieves all expenses for the current user from the database. It queries the ExpenseModel table and filters the results based on the user_id of the current user. If no expenses are found, it raises an HTTPException with a 404 status code. Otherwise, it returns a list of expenses for the current user.
def view_expense(db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    view = db.query(ExpenseModel).filter(ExpenseModel.user_id == current_user.id).all()
    if view is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No expenses found for the current user",
        )
    return view

# view_single_expense endpoint retrieves a single expense by its ID for the current user from the database
@router.get("/View_expense/{id}",
            response_model= ExpenseResponse,
            status_code=status.HTTP_200_OK,
)

#view_single_expense function retrieves a single expense by its ID for the current user from the database. It queries the ExpenseModel table and filters the results based on the expense ID and the user_id of the current user. If no expense is found, it raises an HTTPException with a 404 status code. Otherwise, it returns the expense details.
def view_single_expense( id : int , db : Session = Depends(get_db) , current_user = Depends(get_current_user) ):
    view = db.query(ExpenseModel).filter(ExpenseModel.id == id ,ExpenseModel.user_id == current_user.id).first()
    if view is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with {id} id not found",
     )
    return view

# update_expense endpoint updates an existing expense by its ID for the current user in the database 
@router.put("/Update_expense/{id}",
        response_model= ExpenseResponse,
        status_code=status.HTTP_200_OK,
)

#update_expense function updates an existing expense by its ID for the current user in the database. It queries the ExpenseModel table and filters the results based on the expense ID and the user_id of the current user. If no expense is found, it raises an HTTPException with a 404 status code. Otherwise, it updates the expense details with the provided data and returns the updated expense.
def update_expense(data:UpdateExpense, id : int , db : Session = Depends(get_db) , current_user = Depends(get_current_user)):
    update = db.query(ExpenseModel).filter(ExpenseModel.id == id , ExpenseModel.user_id == current_user.id).first()
    if update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with {id} id not found",
    )
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(update,field,value)

    db.commit()
    db.refresh(update)

    return update

# delete_expense endpoint delete an existing expense by its ID for the current user in the database 
@router.delete("/delete_expense/{id}",
        response_model= ExpenseResponse,
        status_code=status.HTTP_200_OK,
)

#delete_expense function delete an existing expense by its ID for the current user in the database. It queries the ExpenseModel table and filters the results based on the expense ID and the user_id of the current user. If no expense is found, it raises an HTTPException with a 404 status code. Otherwise, it delete the expense details with the provided id and returns the snapshot of deleted expense.
def delete_expense(id : int , db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    delete = db.query(ExpenseModel).filter(ExpenseModel.id == id , ExpenseModel.user_id == current_user.id).first()
    if delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with {id} id not found",
        )
    response_data = ExpenseResponse.model_validate(delete)
    db.delete(delete)
    db.commit()
    return response_data


    
    