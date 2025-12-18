from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.categories import BookCategory


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=True)
    author = relationship("Author", back_populates="books")

    category = Column(
        SqlEnum(BookCategory, name="book_category"),
        nullable=False,
        default=BookCategory.AUTRE,
    )
