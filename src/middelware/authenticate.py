from fastapi import Request
import bcrypt
from passlib.context import CryptContext
from datetime import datetime, timedelta  
from utils.config import SECRET_KEY, JWT_ALGORITHM, JWT_AUDIENCE, JWT_TOKEN_PREFIX, ACCESS_TOKEN_EXPIRE_MINUTES
from data.user import UserPasswordUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def authenticate(request: Request, call_next):
        # TODO - cert auth : get fields passed by apache (https://stackoverflow.com/a/7691293) -> get user with infos
        # TODO - dev : user pass the headers he wants to in his request
        return await call_next(request)

class AuthException(BaseException):
    """
    Custom auth exception that can be modified later on.
    """
    pass

class AuthSrvice:
    
    
    def create_salt_and_hashed_password(self, plaintext_password: str):
        salt = self.generate_salt()
        hashed_password = self.hash_password(password=plaintext_password, salt=salt)
        return salt, hashed_password

    def generate_salt(self):
        return bcrypt.gensalt().decode()
    
    def hash_password(self,*, password: str, salt: str):
        return pwd_context.hash(password + salt)

    def verify_password(self, *, password: str, salt: str, hashed_pw: str):
        return pwd_context.verify(password + salt, hashed_pw)


