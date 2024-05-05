import os
import random
import string
from datetime import datetime
from typing import List


from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session, joinedload

from data.articles import ArticleBase, ArticleCreate, Article, ArticleModel, Tag, TagBase, TagModel
from utils.convert import resize_image, convert_jpg_to_webp, tattoo_image

class ArticleController:

  @staticmethod
  def get_articles(db: Session, limit: int = 10):
    if db is None:
      raise HTTPException(status_code=404, detail="Articles not found")
    else:
      result = db.query(ArticleModel).options(joinedload(ArticleModel.tags)).limit(limit).all()
      if result is None:
        raise HTTPException(status_code=404, detail="Articles not found")
    return result
  
  @staticmethod
  def create_article(db: Session, article: ArticleCreate, file: UploadFile, list_tags: List[Tag]):
    file_name = upload_file(file)
    file_name_without_ext = os.path.splitext(file_name)[0]
    # convert the image to webp
    convert_jpg_to_webp(f"uploads/{file_name}", f"uploads/{file_name_without_ext}.webp")
    file_name = f"{file_name_without_ext}.webp"
    # tatto the file
    tattoo_image(f"uploads/{file_name}", f"utils/watermark.png", f"uploads/fullsize/{file_name}")
    # resize the image
    resize_image(f"uploads/fullsize/{file_name}", f"uploads/thumbnails/{file_name}", (200, 200))
    
    db_article = ArticleModel(
      nom=article.nom,
      path=f'fullsize/{file_name}',
      thumbnail=f'thumbnails/{file_name}',  
      description=article.description,
      date_creation=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    for tag in list_tags:
      db_tag = db.query(TagModel).filter(TagModel.id == tag.id).first()
      db_article.tags.append(db_tag)
    db.commit()
    return db_article
  
  @staticmethod
  def get_article_by_id(db: Session, article_id: int):
    return db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
  
  @staticmethod
  def get_lasts_articles(db: Session, limit: int = 10):
    return db.query(ArticleModel).order_by(ArticleModel.date_creation.desc()).limit(limit).all()
  
def upload_file(file: UploadFile):
  file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
  with open(os.path.join("uploads", file_name), "wb") as file_object:
    file_object.write(file.file.read())
  return file_name

def modify_article(db: Session, article_id: int, article: ArticleBase):
  db_article = db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
  if db_article is None:
    raise HTTPException(status_code=404, detail="Article not found")
  db_article.nom = article.nom
  db_article.taille = article.taille
  db_article.emplacement = article.emplacement
  db_article.type = article.type
  db_article.description = article.description
  db.commit()
  db.refresh(db_article)
  return db_article