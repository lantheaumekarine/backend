import resend
from fastapi import APIRouter
from typing import List
from data.email import Email

resend.api_key = "re_gxB2fTeB_8fbTCn6L2enwQaA3ALUK8npd"

router = APIRouter(
  prefix="/mailing",
  tags=["mailing"],
  dependencies=[]
)

@router.post("/send")
def send_mail(email: Email):
  name = email.name
  phone = email.phone
  Email = email.email
  Service = email.service
  return resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": "brnrcamille@gmail.com", 
    "subject": Service,
    "html":  f"Message from: {name} <br>Phone: {phone}<br>Email: {Email}<br>Service: {Service}"
    })