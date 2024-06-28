import os
import random
import string
from datetime import datetime
from typing import List

from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from data.user import UserCreate, User, UserModify

class UserController:

  @staticmethod
  def create_user(db: Session, user: UserCreate):
    db_user = User(
      username=user.username,
      email=user.email,
      password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

  @staticmethod
  def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

  @staticmethod
  def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

  @staticmethod
  def get_users(db: Session, limit: int = 10):
    if db is None:
      raise HTTPException(status_code=404, detail="Users not found")
    else:
      result = db.query(User).limit(limit).all()
      if result is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return result

  @staticmethod
  def modify_user(db: Session, user_id: int, user: UserModify):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    return db_user

  @staticmethod
  def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user
  
  @staticmethod
  def login(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    if db_user.password != user.password:
      raise HTTPException(status_code=401, detail="Invalid password")
    return db_user