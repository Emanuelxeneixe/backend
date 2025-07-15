from pydantic import BaseModel, ConfigDict, Field


class LibroCreate(BaseModel):
    titulo: str = Field(..., title="Titulo del libro", description="Titulo del libro", max_length=20)
    autor: str = Field(..., title="Autor del libro", description="Autor del libro", pattern="^[A-Za-z\s]*$")
    precio: float = Field(..., gt=0, lt=100000)

class Libro(LibroCreate):
    id: int
    
    model_config = ConfigDict(from_attributes=True)




   # class Config:
   #     orm_mode = True