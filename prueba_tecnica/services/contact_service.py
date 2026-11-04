from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.phone import Phone
from models.contact_phone import ContactPhone
from models.contact import Contact
from repositories.contact_repository import ContactRepository

class ContactService:
    @staticmethod
    def create_contact(db: Session, request):
        existing = ContactRepository.get_by_email(db, request.email)

        if existing:
            raise HTTPException(status_code=409, detail= "Email exists")
        contact = Contact(first_name= request.first_name, last_name= request.last_name, email= request.email)

        for phone_data in request.phones:
            phone = (db.query(Phone).filter(Phone.number == phone_data.number).first())

            if not phone:
                phone = Phone(number=phone_data.number)

                db.add(phone)
                db.flush()
            relation = ContactPhone(phone = phone, type = phone_data.type)
            contact.phones.append(relation)

        return ContactRepository.save(db,contact)
    @staticmethod
    def get_contact(db: Session,contact_id: int):
        contact= ContactRepository.get_by_id(db, contact_id)
        if not contact: 
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact
    @staticmethod
    def delete_contact(db: Session, contact_id: int):
        contact= ContactRepository.get_by_id(db,contact_id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        contact.is_active = False
        db.commit()
    @staticmethod
    def list_contacts(db: Session, skip: int = 0, limit: int = 10):
        return ContactRepository.get_all(db, skip,limit)

    @staticmethod
    def update_contact(db: Session, contact_id: int, request):
        contact= ContactRepository.get_by_id(db,contact_id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        email_owner=(ContactRepository.get_by_email(db,request.email))
        if (email_owner and email_owner.id != contact.id):
            raise HTTPException(status_code=409, detail="email already exist")
        contact.first_name= request.first_name
        contact.last_name= request.last_name
        contact.email=request.email
        db.commit()
        db.refresh(contact)
        return contact