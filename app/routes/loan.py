from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.core.database import get_db
from app.models.loan import Loan
from app.models.book import Book
from app.schemas.loan import LoanCreate, LoanRead

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", response_model=LoanRead, status_code=status.HTTP_201_CREATED)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livre introuvable")

    if book.available_copies <= 0:
        raise HTTPException(status_code=400, detail="Livre non disponible")

    due_date = datetime.utcnow() + timedelta(days=14)

    new_loan = Loan(
        borrower_name=loan.borrower_name,
        borrower_email=loan.borrower_email,
        library_card_number=loan.library_card_number,
        book_id=loan.book_id,
        due_date=due_date,
    )

    book.available_copies -= 1

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return new_loan

@router.get("/", response_model=list[LoanRead])
def get_loans(db: Session = Depends(get_db)):
    return db.query(Loan).all()

@router.put("/{loan_id}/return", response_model=LoanRead)
def return_loan(loan_id: int, db: Session = Depends(get_db)):

    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Emprunt introuvable")

    if loan.return_date:
        raise HTTPException(status_code=400, detail="Livre déjà retourné")

    loan.return_date = datetime.utcnow()
    loan.status = "retourné"

    loan.book.available_copies += 1

    db.commit()
    db.refresh(loan)

    return loan
