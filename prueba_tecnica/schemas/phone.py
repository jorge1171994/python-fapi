from pydantic import BaseModel

class PhoneCreate(BaseModel):
    number: str
    type: str

class PhoneData(BaseModel):
    id: int
    number: str
    class Config: 
        from_attributes = True

class PhoneResponse(BaseModel):
    id: int
    number: str
    type: str

    class Config: 
        from_attributes = True