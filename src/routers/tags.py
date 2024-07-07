from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from typing import List

from data.articles import Tag, TagBase, TagCreate
from utils.database import get_db
from controllers.tags import TagController
from utils.config import manager

router = APIRouter(
  prefix="/tags",
  tags=["tags"],
  dependencies=[]
)

@router.get("/", response_model=List[Tag])
def get_all_tags(db: Session = Depends(get_db)):
  return TagController.get_all_tags(db)

@router.post("/")
def create_tag(tag: TagCreate, db: Session = Depends(get_db), user = Depends(manager)):
  return TagController.create_tag(db, tag)

@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db), user = Depends(manager)):
  return TagController.delete_tag(db, tag_id)

@router.put("/{tag_id}")
def modify_tag(tag_id: int, tag: TagBase, db: Session = Depends(get_db), user = Depends(manager)):
  return TagController.modify_tag(db, tag_id, tag)

@router.get("/{tag_id}")
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
  return TagController.get_tag_by_id(db, tag_id)