from starlette.config import Config
from starlette.datastructures import Secret
from fastapi_login import LoginManager

config = Config(".env")
SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    cast=int,
    default=7 * 24 * 60  # one week
)
JWT_ISSUER = config("JWT_ISSUER", cast=str)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str, default="HS256")
JWT_AUDIENCE = config("JWT_AUDIENCE", cast=str)
JWT_TOKEN_PREFIX = config("JWT_TOKEN_PREFIX", cast=str, default="Bearer")

manager = LoginManager(
    secret=config("SECRET_KEY"),
    token_url="/users/login"
)