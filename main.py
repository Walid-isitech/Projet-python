from fastapi import FastAPI
from Projet.database import engine, Base
from Projet.models import author
from Projet.routes import author


app = FastAPI(title="Library API")

Base.metadata.create_all(bind=engine)

app.include_router(author.router)


@app.get("/")
def root():
    return {"message": "API Bibliothèque lancée"}
