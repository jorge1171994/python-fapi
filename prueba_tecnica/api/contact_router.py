from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.contact import ContactCreate, ContactResponse, ContactUpdate
from services.contact_service import ContactService


router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/",response_model=ContactResponse, status_code=status.HTTP_201_CREATED, summary="Contact Created")
def create_contact(request: ContactCreate, db: Session = Depends(get_db)):
    return ContactService.create_contact(db=db, request=request)

@router.get("", response_model=list[ContactResponse],status_code=status.HTTP_200_OK, summary="Get all")
def get_contacts(
    skip: int =Query(default=0, ge=0, description="Skip records"),
    limit: int = Query(default=10, ge=1, le=100, description="max records returned"),db: Session = Depends(get_db)): 
    return ContactService.list_contacts(db=db, skip=skip, limit=limit)

@router.get("/{contact_id}", response_model=ContactResponse, status_code=status.HTTP_200_OK, summary="contact by id")
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return ContactService.get_contact(db=db, contact_id=contact_id)

@router.put("/{contact_id}", response_model=ContactResponse, status_code=status.HTTP_200_OK, summary="Updated contact")
def update_contact(contact_id: int, request: ContactUpdate, db: Session = Depends(get_db)):
    return ContactService.update_contact(db=db, contact_id=contact_id, request=request)

@router.delete("/{contact_id}", status_code= status.HTTP_204_NO_CONTENT, summary= "Soft delete")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    ContactService.delete_contact(db=db, contact_id=contact_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)