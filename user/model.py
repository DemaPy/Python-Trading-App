from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, server_default='TRUE')
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, server_default='TRUE', nullable=False)
    is_superuser = Column(Boolean, server_default='FALSE', nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))