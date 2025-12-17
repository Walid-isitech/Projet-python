from fastapi import FastAPI

from app.database import engine
from app.core.database import Base

from app.models.book import Book
from app.models.author import Author
from app.models.loan import Loan

from app.routes.book import router as book_router
from app.routes.author import router as author_router
from app.routes.loan import router as loan_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(book_router)
app.include_router(author_router)


app.include_router(loan_router)
