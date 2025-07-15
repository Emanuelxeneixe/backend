from database import Base
from sqlalchemy import Column, Integer, String, Float


class LibrosModel(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    precio = Column(Float)
    
   