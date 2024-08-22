from fastapi import Request
import bcrypt


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
        salt = self.generate_salt().decode('utf-8')
        hashed_password = self.hash_password(password=plaintext_password, salt=salt)
        return salt, hashed_password

    def generate_salt(self):
        return bcrypt.gensalt()
    
    def hash_password(self,*, password: str, salt: str):
        return bcrypt.hashpw(password.encode(),salt.encode()).decode('utf-8')

    def verify_password(self, *, password: str, salt: str, hashed_pw: str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8'))


