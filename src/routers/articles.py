from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List

from data.articles import Article, ArticleCreate, Tag
from utils.database import get_db
from controllers.articles import ArticleController

from controllers.tags import TagController

import logging

logger = logging.getLogger(__name__)

router = APIRouter(
  prefix="/articles",
  tags=["articles"],
  dependencies=[]
)

@router.get("/", response_model=List[Article])
def get_articles(db: Session = Depends(get_db), limit: int = 10):
  return ArticleController.get_articles(db,limit)

@router.get("/lasts", response_model=List[Article])
def get_lasts_articles(db: Session = Depends(get_db), limit: int = 10):
  return ArticleController.get_lasts_articles(db,limit)


@router.get("/{article_id}", response_model=Article)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
  return ArticleController.get_article_by_id(db, article_id)

@router.post("/")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
  list_tags = []
  for tag in article.tags:
    print(tag)  
    tag = TagController.get_tag_by_name(db, tag)
    d_tag = Tag(id=tag.id, tag=tag.tag)
    list_tags.append(d_tag)
  return ArticleController.create_article(db, article, list_tags)

@router.put("/{article_id}")
def modify_article(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
  return ArticleController.modify_article(db, article_id, article)

@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
  return ArticleController.delete_article(db, article_id)
