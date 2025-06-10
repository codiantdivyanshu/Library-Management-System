from pydantic import BaseModel
from typing import Optional

class Author(BaseModel):
    id: int
    name: str
    bio: Optional[str] = None  # Short biography or description

    class Config:
        from_attributes = True  # Pydantic v2 compatible

