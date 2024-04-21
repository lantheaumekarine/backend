import string
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from data.tags import TagBase, TagModel

@staticmethod
def get_all_tags(db: Session):
    return db.query(TagModel).all()

@staticmethod
def create_tag(db: Session, tag: TagBase):
    db_tag = TagModel(
        tag=tag.tag
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

@staticmethod
def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(db_tag)
    db.commit()
    return db_tag

def modify_tag(db: Session, tag_id: int, tag: TagBase):
    db_tag = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    db_tag.tag = tag.tag
    db.commit()
    db.refresh(db_tag)
    return db_tag

