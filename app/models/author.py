
from datetime import date
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    """Table des auteurs"""

    __tablename__ = "authors"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    birth_date: date
    country_iso: str = Field(max_length=2)  # Code ISO du pays
    bio: Optional[str] = None
    death_date: Optional[date] = None
    website_url: Optional[str] = None

    # Relation avec les livres
