from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List

class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    taille = Column(Integer)
    emplacement = Column(String)
    type = Column(String)
    description = Column(Text, nullable=True)
    date_creation = Column(String)
    tags = relationship("TagModel", back_populates="article")


#Scheme for Article
class ArticleBase(BaseModel):
    nom: str
    taille: int
    emplacement: str
    type: str
    description: Optional[str]
    tags: Optional[List[str]] = []
class Article(ArticleBase):
    id: int
    date_creation: str
    class Config:
        orm_mode = True

class ArticleCreate(BaseModel):
    nom: str
    description: Optional[str]
    emplacement: str
    tags: Optional[List[str]] = []
    pass
