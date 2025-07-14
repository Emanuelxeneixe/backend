from pydantic import BaseModel, ConfigDict

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    precio: float

class Libro(LibroCreate):
    id: int
    
    model_config = ConfigDict(from_attributes=True)




   # class Config:
   #     orm_mode = True