from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import HTTPException
from Projet.database import SessionLocal
from Projet.models.author import Author
from Projet.schemas.author import AuthorCreate, AuthorResponse
from typing import List


router = APIRouter(prefix="/authors", tags=["Authors"])


# Dépendance pour la session BDD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(
        first_name=author.first_name,
        last_name=author.last_name,
        birth_date=author.birth_date
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.get("/", response_model=List[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return authors

@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()

    if author is None:
        raise HTTPException(status_code=404, detail="Auteur non trouvé")

    return author
