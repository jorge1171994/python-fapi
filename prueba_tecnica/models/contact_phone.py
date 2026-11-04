from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
#import Base de models
from core.database import Base

class ContactPhone(Base):
    __tablename__ = "contact_phones"
    contact_id = Column(Integer, ForeignKey("contacts.id"), primary_key = True)
    phone_id = Column(Integer, ForeignKey("phones.id"), primary_key = True)
    contact = relationship("Contact", back_populates  = "phones")
    phone = relationship("Phone", back_populates = "contacts")
    type = Column(String(20), nullable=False)