from fastapi import APIRouter
from schemas import LibroCreate
librosRoute = APIRouter()

@librosRoute.get("/")
def read_root():
    return {"Hello": "World"}

@librosRoute.get("/libro/{id}")
def read_libro(id: int):
    return {"id": id}

@librosRoute.post("/libro/")
def create_libro(Libro: LibroCreate):
    return {"ok"}