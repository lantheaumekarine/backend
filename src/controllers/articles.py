import os
import random
import string
from datetime import datetime

from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from data.articles import ArticleModel

class ArticleController:

  @staticmethod
  def get_articles(db: Session, limit: int = 10):
    return db.query(ArticleModel).limit(limit).all()
  
  @staticmethod
  def create_article(db: Session, article: ArticleModel):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
  
  @staticmethod
  def get_article_by_id(db: Session, article_id: int):
    return db.query(ArticleModel).filter(ArticleModel.id == article_id).first()