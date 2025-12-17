from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


class LoanBase(BaseModel):
    borrower_name: str
    borrower_email: EmailStr
    library_card_number: str
    book_id: int


class LoanCreate(LoanBase):
    pass


class LoanRead(LoanBase):
    id: int
    loan_date: datetime
    due_date: datetime
    return_date: Optional[datetime]
    status: str
    comment: Optional[str]

    class Config:
        orm_mode = True
