from typing import Optional, List

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base

from data.articles import ArticleBase

class TagModel(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, index=True)
    article = relationship("ArticleModel", secondary="tags_articles", back_populates="tags")

#Scheme for Tag
class TagBase(BaseModel):
    id: int
    tag: str

class Tag(TagBase):
    articles: Optional[List[ArticleBase]] = []

    class Config:
        orm_mode = True