from fastapi import FastAPI
from src.database.base import Base
from src.database.session import engine
from src.models.expense import ExpenseModel
from src.routers import services


Base.metadata.create_all(engine)


app = FastAPI(
    title="HisabKeep",
    version="0.1.0",
)
app.include_router(services.router)

@app.get("/")
def root():
    return {"message": "Welcome To HisabKeep"}
