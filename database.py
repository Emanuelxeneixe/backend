from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# String o cadena de conexión a la base de datos

DB_URL = "postgresql://postgres:postgres@localhost:5432/libreria"
# DB_URL = "sqlite:///./libreria.db"  # Cambia esto según tu base de datos

# Crear un motor de base de datos
engine = create_engine(DB_URL)

# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Adicionales
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
