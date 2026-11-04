from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine
from core.database import Base
from models.contact import Contact
from models.phone import Phone
from models.contact_phone import ContactPhone
from api.contact_router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    #genera tablas
    Base.metadata.create_all(bind=engine)

    yield

app=FastAPI(lifespan = lifespan)


app.include_router(router)



@app.get("/health")
def health_check():
    return {"status" : "up"}
