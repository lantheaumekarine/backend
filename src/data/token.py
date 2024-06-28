from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from tools.config import JWT_ISSUER, JWT_AUDIENCE, ACCESS_TOKEN_EXPIRE_MINUTES



class JWTMeta(BaseModel):
    iss: str = JWT_ISSUER
    aud: str = JWT_AUDIENCE
    iat: float = datetime.timestamp(datetime.utcnow())
    exp: float = datetime.timestamp(datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
class JWTCreds(BaseModel):
    """How we'll identify users"""
    sub: str
    username: str
class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """
    pass
class AccessToken(BaseModel):
    access_token: str
    token_type: str