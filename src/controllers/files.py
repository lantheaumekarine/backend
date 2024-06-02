import os
import random
import string
from datetime import datetime
from typing import List

from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from data.files import FileBase, File, FileModel
from data.articles import ArticleModel
from utils.convert import resize_image, convert_jpg_to_webp, tattoo_image


class FileController:

  @staticmethod
  def create_file(db: Session, file: UploadFile):
    file_name = upload_file(file)
    file_name_without_ext = os.path.splitext(file_name)[0]
    # convert the image to webp
    convert_jpg_to_webp(f"uploads/{file_name}", f"uploads/{file_name_without_ext}.webp")
    file_name = f"{file_name_without_ext}.webp"
    # tatto the file
    tattoo_image(f"uploads/{file_name}", f"utils/watermark.png", f"uploads/fullsize/{file_name}")
    # resize the image
    resize_image(f"uploads/fullsize/{file_name}", f"uploads/thumbnails/{file_name}", (200, 200))
    db_file = FileModel(
      nom=file_name
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
  
  def get_file_by_id(db: Session, file_id: int):
    return db.query(FileModel).filter(FileModel.id == file_id).first()
  
  @staticmethod
  def delete_file(db: Session, file_id: int):
    db_file = db.query(FileModel).filter(FileModel.id == file_id).first()
    if db_file is None:
      raise HTTPException(status_code=404, detail="File not found")
    # Get the related Article
    db_article = db.query(ArticleModel).filter(ArticleModel.file_id == file_id).first()
    if db_article is not None:
      db_article.file_id = None
      db.commit()
      
    os.remove(f"uploads/fullsize/{db_file.nom}")
    os.remove(f"uploads/thumbnails/{db_file.nom}")
    db.delete(db_file)
    db.commit()
    return db_file


def upload_file(file: UploadFile):
  file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
  with open(os.path.join("uploads", file_name), "wb") as file_object:
    file_object.write(file.file.read())
  return file_name