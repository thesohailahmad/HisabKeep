from fastapi import FastAPI
from src.database.base import Base
from src.database.session import engine
from src.models.expense import ExpenseModel
from src.routers import expense_services , user_services
from src.models.user import UserModel

# Create the database tables
Base.metadata.create_all(engine)

# expose the FastAPI app
app = FastAPI(
    title="HisabKeep",
    version="1.1.0",
)

# Include the routers for expense and user services
app.include_router(expense_services.router)
app.include_router(user_services.router)

# get the root endpoint
@app.get("/")
def root():
    return {"message": "Welcome To HisabKeep"}
