from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  , declarative_base , Session
from src.database.db import settings
from typing import Generator

Base = declarative_base()
engine = create_engine(url=settings.DB_CONNECTION , pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield(db)
    finally:
        db.close()