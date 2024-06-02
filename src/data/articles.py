from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List
from .files import File


# Declare Classes / Tables
tags_articles = Table('tags_articles', Base.metadata,
    Column('article_id', ForeignKey('article.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True)
)


class ArticleModel(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(Text, nullable=True)
    date_creation = Column(String)
    tags = relationship("TagModel", secondary="tags_articles", back_populates="articles")

    # Add a foreign key to the File model
    file_id = Column(Integer, ForeignKey('file.id'))

    # Add a relationship to the File model
    file = relationship("FileModel", back_populates="article")


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
    tags: Optional[List[TagBase]] = []
    file: Optional[File] = None
    date_creation: str

    class Config:
        orm_mode = True

class ArticleCreate(ArticleBase):
    file_id: int
    tags: List[str]

    class Config:
        orm_mode = True
