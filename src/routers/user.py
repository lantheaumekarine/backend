from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from data.user import User, UserCreate, UserModify
from utils.database import get_db
from controllers.user import UserController
from fastapi.security import OAuth2PasswordRequestForm

import logging

logger = logging.getLogger(__name__)

router = APIRouter(
  prefix="/users",
  tags=["users"],
  dependencies=[]
)

@router.get("/", response_model=List[User]) 
def get_users(db: Session = Depends(get_db), limit: int = 10):
  return UserController.get_users(db, limit)

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  return UserController.create_user(db, user)

@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  return UserController.get_user_by_id(db, user_id)

@router.get("/email/{email}", response_model=User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
  return UserController.get_user_by_email(db, email)

@router.patch("/{user_id}")
def modify_user(user_id: int, user: UserModify, db: Session = Depends(get_db)):
  return UserController.modify_user(db, user_id, user)

@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db) ):
    return UserController.user_login(db=db, user_username=data.username, user_password=data.password)
