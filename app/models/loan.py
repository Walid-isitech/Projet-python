from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)

    borrower_name = Column(String, nullable=False)
    borrower_email = Column(String, nullable=False)
    library_card_number = Column(String, nullable=False)

    loan_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)

    status = Column(String, default="actif", nullable=False)
    comment = Column(String, nullable=True)

    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    book = relationship("Book", back_populates="loans")
