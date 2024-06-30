from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String
from utils.database import Base

class UserDB(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)
  salt = Column(String)



# Schema
class UserBase(BaseModel):
    username: str
    password: constr(min_length=7, max_length=100)
    email: str

class UserPasswordUpdate(UserBase):
    """
    Users can change their password
    """
    password: constr(min_length=7, max_length=100)
    salt: str


class UserCreate(UserBase):
    pass

    

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserAuthenticated(UserPasswordUpdate):
    pass

class UserModify(User):
  email: str
  password: str