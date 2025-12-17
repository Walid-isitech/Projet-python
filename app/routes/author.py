from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Projet.models.author import Author
from Projet.schemas.author import AuthorCreate, AuthorResponse
from Projet.core.database import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(
        first_name=author.first_name,
        last_name=author.last_name
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.get("/", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()
