from sqlalchemy import create_engine #para conexion
from sqlalchemy.ext.declarative import declarative_base #Crear la clase de la base
from sqlalchemy.orm import sessionmaker #crear las sesiones

#Url para conexion local a SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#Crear el motor de sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False})

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()