from datetime import datetime
from pydantic import BaseModel, EmailStr
from schemas.phone import PhoneCreate
from schemas.phone import PhoneResponse

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phones: list[PhoneCreate]

class ContactUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    phones: list[PhoneResponse]
    class Config:
        from_attributes = True