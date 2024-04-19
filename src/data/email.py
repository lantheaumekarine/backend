from pydantic import BaseModel

class Email(BaseModel):
  name: str
  phone: str
  email: str
  service: str