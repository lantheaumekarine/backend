from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from starlette.config import Config

config = Config(".env")

SQLALCHEMY_SQLITE_URL = "sqlite:///./test.db"
SQLALCHEMY_PGSQL_URL = "postgresql://webuser:password@localhost/test"

engine = create_engine(
    # SQLITE
    SQLALCHEMY_SQLITE_URL, connect_args={"check_same_thread": False}
    # POSTGRES
    #SQLALCHEMY_PGSQL_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

ALLOW_ORIGINS = config("ALLOW_ORIGINS", cast=str)
# Database SessionLocal Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
