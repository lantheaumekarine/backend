from fastapi import APIRouter, Depends, UploadFile
from fastapi import File as FileField
from sqlalchemy.orm import Session
from typing import List

from data.files import File
from utils.database import get_db
from controllers.files import FileController

import logging

logger = logging.getLogger(__name__)

router = APIRouter(
  prefix="/files",
  tags=["files"],
  dependencies=[]
)

@router.post("/")
def create_file(file: UploadFile = FileField(...), db: Session = Depends(get_db)):
  return FileController.create_file(db, file)

@router.get("/{file_id}", response_model=File)
def get_file_by_id(file_id: int, db: Session = Depends(get_db)):
  return FileController.get_file_by_id(db, file_id)

@router.delete("/{file_id}")
def delete_file(file_id: int, db: Session = Depends(get_db)):
  return FileController.delete_file(db, file_id)
  

