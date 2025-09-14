from dotenv import load_dotenv
load_dotenv()
from database import engine, Base, get_db
from user.model import User
from user.schemas import CreateUser
from sqlalchemy.orm import Session
from typing import List
from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI, Depends
from auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")
    yield  # <-- Application runs here
    # Shutdown: cleanup if needed
    print("🛑 App is shutting down.")

app = FastAPI(lifespan=lifespan)

@app.get('/users', response_model=List[CreateUser])
def users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return  users

app.include_router(auth_router)