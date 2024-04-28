from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List

from data.tags import TagBase

# Declare Classes / Tables
book_authors = Table('tags_articles', Base.metadata,
    Column('article_id', ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)


class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    emplacement = Column(String)
    description = Column(Text, nullable=True)
    date_creation = Column(String)
    tags = relationship("TagModel", secondary="tags_articles", back_populates="article")


#Scheme for Article
class ArticleBase(BaseModel):
    nom: str
    description: Optional[str]
class Article(ArticleBase):
    id: int
    tags: Optional[List[TagBase]] = []
    date_creation: str
    class Config:
        orm_mode = True

class ArticleCreate(ArticleBase):
    tags: Optional[List[TagBase]] = []
    pass

    class Config:
        orm_mode = True
