from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base


class FileModel(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)

    # Add a relationship to the Article model
    article = relationship("ArticleModel", uselist=False, back_populates="file")

class FileBase(BaseModel):
    nom: str

class File(FileBase):
    id: int

    class Config:
        orm_mode = True