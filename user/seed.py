from dotenv import load_dotenv
load_dotenv()
from faker import Faker
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from user.model import User
import random
import bcrypt

Base.metadata.create_all(bind=engine)

faker = Faker()

def create_fake_user():
    password = faker.password(length=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    return User(
        username=faker.user_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.unique.email(),
        is_active=random.choice([True, False]),
        is_superuser=random.choice([True, False]),
        hashed_password=hashed_password
    )

def populate_users(n: int = 10):
    db: Session = next(get_db())
    for _ in range(n):
        user = create_fake_user()
        db.add(user)
    db.commit()
    db.close()
    print(f"✅ {n} fake users added to the database.")

if __name__ == "__main__":
    populate_users(10)
