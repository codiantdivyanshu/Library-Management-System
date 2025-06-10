
from typing import List, Optional
from app.schemas.book_schemas import Book
from app.schemas.member_schemas import Member

class LibraryService:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []

    # --- Book Operations ---
    def add_book(self, book: Book):
        self.books.append(book)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.id == book_id), None)

    def get_all_books(self) -> List[Book]:
        return self.books

    def remove_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False

    # --- Member Operations ---
    def add_member(self, member: Member):
        self.members.append(member)

    def get_member_by_id(self, member_id: int) -> Optional[Member]:
        return next((m for m in self.members if m.id == member_id), None)

    def get_all_members(self) -> List[Member]:
        return self.members

    def remove_member(self, member_id: int) -> bool:
        member = self.get_member_by_id(member_id)
        if member:
            self.members.remove(member)
            return True
        return False

    # --- Borrowing / Returning ---
    def borrow_book(self, book_id: int, member_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        member = self.get_member_by_id(member_id)
        if book and not book.is_borrowed and member:
            book.is_borrowed = True
            book.borrowed_by = member_id
            return True
        return False

    def return_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book and book.is_borrowed:
            book.is_borrowed = False
            book.borrowed_by = None
            return True
        return False

