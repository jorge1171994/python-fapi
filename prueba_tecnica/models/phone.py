from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
#import from database
from core.database import Base

class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key = True)
    number = Column(String(20), nullable = False, unique = True)
    contacts = relationship("ContactPhone", back_populates = "phone")
