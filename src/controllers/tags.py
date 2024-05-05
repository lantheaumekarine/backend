import string

from fastapi import HTTPException
from sqlalchemy.orm import Session

from data.articles import TagBase, TagModel, TagCreate
class TagController:
    @staticmethod
    def get_all_tags(db: Session):
        if db is None:
            raise HTTPException(status_code=404, detail="Tags not found")
        else:
            result = db.query(TagModel).all()
            if result is None:
                raise HTTPException(status_code=404, detail="Tags not found")
            return result

    @staticmethod
    def create_tag(db: Session, tag: TagCreate):
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
    
    def get_tag_by_id(db: Session, tag_id: int):
        return db.query(TagModel).filter(TagModel.id == tag_id).first()
    
    def get_tag_by_name(db: Session, tag_name: str):
        return db.query(TagModel).filter(TagModel.tag == tag_name).first()

