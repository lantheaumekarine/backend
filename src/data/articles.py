
from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base

class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    taille = Column(Integer)
    emplacement = Column(String)
    type = Column(String)
    description = Column(Text, nullable=True)
    date_creation = Column(String)

#Scheme for Article
class ArticleBase(BaseModel):
    nom: str
    taille: int
    emplacement: str
    type: str
    description: Optional[str]
class Article(ArticleBase):
    id: int
    date_creation: str
    class Config:
        orm_mode = True

class ArticleCreate(ArticleBase):
    pass
