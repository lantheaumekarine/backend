from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List

# Declare Classes / Tables
book_authors = Table('tags_articles', Base.metadata,
    Column('article_id', ForeignKey('article.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
)


class ArticleModel(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    path = Column(String)
    thumbnail = Column(String)
    description = Column(Text, nullable=True)
    date_creation = Column(String)
    tags = relationship("TagModel", secondary="tags_articles", back_populates="articles")


class TagModel(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, index=True)
    articles = relationship("ArticleModel", secondary="tags_articles", back_populates="tags")

#Scheme for Article
class ArticleBase(BaseModel):
    nom: str
    description: Optional[str]

#Scheme for Tag
class TagBase(BaseModel):
    id: int
    tag: str

    class Config:
        orm_mode = True

class TagCreate(BaseModel):
    tag: str

class Tag(TagBase):
    pass
class Article(ArticleBase):
    id: int
    path: str
    thumbnail: str
    tags: Optional[List[TagBase]] = []
    date_creation: str

    class Config:
        orm_mode = True

class ArticleCreate(ArticleBase):
    pass

    class Config:
        orm_mode = True
