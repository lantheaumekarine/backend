import os
import random
import string
from datetime import datetime

from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from data.articles import ArticleBase, ArticleCreate, Article, ArticleModel

class ArticleController:

  @staticmethod
  def get_articles(db: Session, limit: int = 10):
    return db.query(ArticleModel).limit(limit).all()
  
  @staticmethod
  def create_article(db: Session, article: ArticleCreate):
    db_article = ArticleModel(
      nom=article.nom,
      taille=article.taille,
      emplacement=article.emplacement,
      type=article.type,
      description=article.description,
      date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
  
  @staticmethod
  def get_article_by_id(db: Session, article_id: int):
    return db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
  
  @staticmethod
  def get_lasts_articles(db: Session, limit: int = 10):
    return db.query(ArticleModel).order_by(ArticleModel.date_creation.desc()).limit(limit).all()