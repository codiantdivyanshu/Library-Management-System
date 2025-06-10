from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    is_borrowed: bool = False
    borrowed_by: Optional[int] = None  # This will hold member ID if borrowed

    class Config:
        from_attributes = True  # Required for Pydantic v2 (replaces orm_mode)


