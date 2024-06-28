from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
import logging
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from middelware.authenticate import authenticate, security

logger = logging.getLogger(__name__)

from utils.database import engine, ALLOW_ORIGINS, SECRET_KEY
from routers import MAIN_ROUTER

import data

data.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = security



app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root_to_docs():
    return RedirectResponse(url="/docs")


for router in MAIN_ROUTER:
    app.include_router(router)