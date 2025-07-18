from fastapi import APIRouter, Depends, HTTPException, status
from schemas import LibroCreate
from sqlalchemy.orm import Session
from database import get_db
from models import LibrosModel 
from schemas import Libro
from typing import Annotated


librosRoute = APIRouter(
prefix = "/libros",
tags = ["Libros"]
)


conn = Annotated[Session, Depends(get_db)]


@librosRoute.get("/", status_code=status.HTTP_200_OK, response_model=list[Libro])  
async def get_libros(db:conn):
    libros = db.query(LibrosModel).all()
    
    return libros

@librosRoute.get("/libro/{id}", status_code=status.HTTP_200_OK, response_model=Libro)
async def get_libro(id: int, db:conn):
    libro = db.query(LibrosModel).filter(LibrosModel.id == id).first()
    
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    
    return libro   
                 
@librosRoute.post("/", status_code=status.HTTP_201_CREATED, response_model=Libro)
async def create_libro(nuevo_libro: LibroCreate, db:conn):
    #libro = LibrosModel(titulo=nuevo_libro.titulo, autor=nuevo_libro.autor, precio=nuevo_libro.precio)
   
    libro = (LibrosModel(**nuevo_libro.model_dump())) #{"titulo": "Mi libro", "autor": "Yo", "precio": 10.0}
    db.add(libro)
    db.commit()
    db.refresh(libro)
    
    return libro
   
@librosRoute.put("/libro/{id}", status_code=status.HTTP_200_OK, response_model=Libro)
async def update_libro(id: int, libro_data: LibroCreate, db:conn):
    libro = db.query(LibrosModel).filter(LibrosModel.id == id).first()

    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")

    #for key, value in libro_data.dict().items():
    #    setattr(libro, key, value)

    libro.titulo = libro_data.titulo
    libro.autor = libro_data.autor
    libro.precio = libro_data.precio

    db.commit()
    db.refresh(libro)

    return libro

@librosRoute.delete("/libro/{id}", status_code=status.HTTP_200_OK, response_model={})
async def delete_libro(id: int, db:conn):
    libro = db.query(LibrosModel).filter(LibrosModel.id == id).first()

    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")

    db.delete(libro)
    db.commit()

    return {"message": "libro eliminado correctamente"}