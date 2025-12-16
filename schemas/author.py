from pydantic import BaseModel
from datetime import date


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: date


class AuthorResponse(AuthorCreate):
    id: int

    class Config:
        orm_mode = True
