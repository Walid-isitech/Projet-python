from pydantic import BaseModel
from .author import AuthorResponse
from app.models.book import BookCategory
from app.schemas.author import AuthorResponse
from app.models.categories import BookCategory
from app.schemas.author import AuthorResponse


class BookCreate(BaseModel):
    title: str
    isbn: str
    author_id: int | None = None
    category: BookCategory = BookCategory.AUTRE


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    category: BookCategory
    author: AuthorResponse | None

    class Config:
        orm_mode = True
