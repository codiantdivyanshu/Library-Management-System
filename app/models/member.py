from typing import List, Optional
from.base import BaseEntity

class Member(BaseEntity):
    """Library member with book borrowing capabilities"""

    def __init__(self, name: str, email:str, phone: Optional[str] = None):
        super().__init__(name)
        self._email: str = email 
        self._phone: Optional[str] = phone 
        self._borrowed_books: List[str]= phone 
        self._borrowed_books: List[str] = []
        self._max_books: int = 5 

    @property 
    def email(self) -> str:
        return self._email 
    
    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value.lower().strip()

    @property 
    def phone(self) -> Optional[str]:
        return self._phone
    
    @phone.setter
    def phone(self, value:Optional [str]):
        self._phone = value.strip() if value else None 

    @property 
    def brorrowed_books(self) -> List[str]:
        return self.borrowed_books.copy()
    
    @property 
    def can_borrrow(self) -> bool: 
        return len(self._borrowed_books) < self._max_books 
    
    def borrow_book(self, book_id: str) -> bool:
        """Add a book to member's borrowed list"""
        if self.can_borrrow and book_id not in self._borrowed_books:
            return True 
        return False 
    
    def return_books(self, book_id: str) -> bool:
        """Remove a book from member's borrowed list """
        if book_id in self._borrowed_books:
            self.brorrowed_books.remove(book_id)
            return True 
        return False 
    
    def to_dict(self) -> dict:
        return { 
            "id": self.id, 
            "name": self.name , 
            "email": self.email ,
            "phone": self.phone, 
            "borrowed_books": self.brorrowed_books, 
            "max_books": self._max_books, 
            "crreated_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat()
        }
