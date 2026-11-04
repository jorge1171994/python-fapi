from sqlalchemy.orm import Session
from models.contact import Contact

class ContactRepository:
    @staticmethod
    def get_by_id(db: Session, contact_id: int):
        return (db.query(Contact).filter(Contact.id == contact_id, Contact.is_active == True).first())
    @staticmethod
    def get_by_email(db: Session, email: str):
        return (db.query(Contact).filter(Contact.email == email).first())
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit =10):
        return (db.query(Contact).filter(Contact.is_active == True).offset(skip).limit(limit).all())
    @staticmethod
    def save(db: Session, contact: Contact):
        db.add(contact)
        db.commit()
        db.refresh(contact)

        return contact
