from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class CreateUser(UserBase):
    class Config:
        orm_mode = True