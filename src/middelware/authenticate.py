from fastapi import FastAPI, Request, Response, HTTPException, Depends
from fastapi.responses import JSONResponse
from base64 import b64decode
from typing import Callable
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def authenticate(credentials:HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "admin"
    correct_username = b64decode(correct_username).decode()
    correct_password = b64decode(correct_password).decode()
    return credentials.username == correct_username and credentials.password == correct_password