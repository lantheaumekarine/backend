from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from typing import List

from data.tags import Tag, TagBase
from utils.database import get_db
from controllers.tags import TagController

router = APIRouter(
  prefix="/tags",
  tags=["tags"],
  dependencies=[]
)

@router.get("/", response_model=List[Tag])
def get_all_tags(db: Session = Depends(get_db)):
  return TagController.get_all_tags(db)

@router.post("/")
def create_tag(tag: TagBase, db: Session = Depends(get_db)):
  return TagController.create_tag(db, tag)

@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
  return TagController.delete_tag(db, tag_id)

@router.put("/{tag_id}")
def modify_tag(tag_id: int, tag: TagBase, db: Session = Depends(get_db)):
  return TagController.modify_tag(db, tag_id, tag)

@router.get("/{tag_id}")
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
  return TagController.get_tag_by_id(db, tag_id)