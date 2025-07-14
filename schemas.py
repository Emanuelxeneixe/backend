from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    precio: float

class Libro(LibroCreate):
    id: int

    class Config:
        orm_mode = True