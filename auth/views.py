from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, crud

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user, error = crud.create_user(db, user)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return db_user
