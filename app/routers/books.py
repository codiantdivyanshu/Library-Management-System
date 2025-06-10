from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.book_schemas import Book

router = APIRouter(prefix="/books", tags=["Books"])

# In-memory storage for books
books_db: List[Book] = []

# Create a new book
@router.post("/", response_model=Book)
def add_book(book: Book):
    if any(b.id == book.id for b in books_db):
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books_db.append(book)
    return book

# Get all books
@router.get("/", response_model=List[Book])
def get_books():
    return books_db

# Get a book by ID
@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book

# Delete a book
@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    books_db.remove(book)
    return book

# Update a book
@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found.")


