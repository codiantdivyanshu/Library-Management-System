from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/authors", tags=["Authors"])

# In-memory author storage (can be replaced with DB)
authors_db = []

# Pydantic schema for Author
class Author(BaseModel):
    id: int
    name: str
    bio: Optional[str] = None

    class Config:
        from_attributes = True

# Create an author
@router.post("/", response_model=Author)
def create_author(author: Author):
    if any(a.id == author.id for a in authors_db):
        raise HTTPException(status_code=400, detail="Author with this ID already exists.")
    authors_db.append(author)
    return author

# Get all authors
@router.get("/", response_model=List[Author])
def get_authors():
    return authors_db

# Get a single author by ID
@router.get("/{author_id}", response_model=Author)
def get_author(author_id: int):
    author = next((a for a in authors_db if a.id == author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return author

# Delete an author
@router.delete("/{author_id}", response_model=Author)
def delete_author(author_id: int):
    author = next((a for a in authors_db if a.id == author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    authors_db.remove(author)
    return author

