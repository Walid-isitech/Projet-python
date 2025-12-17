from pydantic import BaseModel


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str


class AuthorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
