from fastapi import FastAPI
from src.database.base import Base
from src.database.session import engine
from src.models.expense import ExpenseModel
from src.routers import services , user_services
from src.models.user import UserModel



Base.metadata.create_all(engine)


app = FastAPI(
    title="HisabKeep",
    version="0.1.0",
)
app.include_router(services.router)
app.include_router(user_services.router)

@app.get("/")
def root():
    return {"message": "Welcome To HisabKeep"}
