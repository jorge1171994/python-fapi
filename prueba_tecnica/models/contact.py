from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
#importar database
from core.database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50),nullable= False)
    last_name = Column(String(50), nullable= False)
    email = Column(String(50), unique=True, nullable= False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default = True)
    phones = relationship("ContactPhone", back_populates = "contact", cascade = "all, delete-orphan")