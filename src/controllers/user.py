import os
import random
import string
from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from data.user import UserCreate, User, UserModify, UserPasswordUpdate, UserDB
from data.token import AccessToken
from middelware.authenticate import AuthSrvice as auth_service

from fastapi_login.exceptions import InvalidCredentialsException

class UserController:

  @staticmethod
  def create_user(db: Session, user: UserCreate):
    auth = auth_service()
    salt, password = auth.create_salt_and_hashed_password(plaintext_password=user.password)
    salty_user = UserPasswordUpdate(**user.dict(), salt = salt)
    salty_user.password = password
    db_user = UserDB(**salty_user.dict())
    print(db_user)
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
  def user_login(db: Session, user_username: str, user_password: str):
    auth = auth_service()
    db_user = db.query(UserDB).filter(UserDB.username == user_username).first()
    if db_user is None:
        raise InvalidCredentialsException
    
    if not auth.verify_password(password=user_password, salt=db_user.salt, hashed_pw=db_user.password):
        raise InvalidCredentialsException
    access_token = AccessToken(access_token=auth.create_access_token_for_user(user=db_user), token_type="bearer")
    return access_token