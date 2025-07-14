from fastapi import FastAPI
from database import Base, engine
from routes import librosRoute

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(librosRoute)