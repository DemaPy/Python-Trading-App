from sqlalchemy.orm import Session
from user.model import User
from passlib.context import CryptContext
from schemas import CreateUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user_data: CreateUser):
    if db.query(User).filter(User.username == user_data.username).first():
        return None, "Username already registered"
    if db.query(User).filter(User.email == user_data.email).first():
        return None, "Email already registered"

    hashed_password = get_password_hash(user_data.password)

    db_user = User(
        username=user_data.username,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user, None
