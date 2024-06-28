from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from utils.database import Base

class UserDB(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)
  salt = Column(String)




class User(BaseModel):
  id: int

  class Config:
    orm_mode = True


class UserCreate(User):
  username: str
  email: str
  password: str
class UserModify(User):
  email: str
  password: str
