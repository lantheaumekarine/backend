from typing import Optional, Text

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from utils.database import Base

class TagModel(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, index=True)

#Scheme for Tag
class TagBase(BaseModel):
    tag: str