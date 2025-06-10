from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class MemberCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)

class MemberUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)

class MemberResponse(BaseModel):
    id: str
    name: str
    email: str
    phone: Optional[str] = None
    borrowed_books: List[str] = []
    max_books: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
