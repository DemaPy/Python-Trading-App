from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr

class CreateUser(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
