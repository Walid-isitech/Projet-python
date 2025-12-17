from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Projet.schemas.book import BookCreate, BookResponse
from Projet.models.book import Book
from Projet.core.database import get_db
from fastapi import HTTPException


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        isbn=book.isbn,
        author_id=book.author_id

    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Livre non trouvé")

    return book
