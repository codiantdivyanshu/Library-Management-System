import json
import os
from typing import Dict, List, Any
from pathlib import Path

class DataStorage:
    """File-based storage service demonstrating file I/O and error handling"""
    
    def __init__(self, data_file: str = "data/library_data.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(exist_ok=True)
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """Create data file if it doesn't exist"""
        if not self.data_file.exists():
            initial_data = {
                "authors": {},
                "books": {},
                "members": {}
            }
            self.save_data(initial_data)
    
    def load_data(self) -> Dict[str, Any]:
        """Load data from JSON file with error handling"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            self._ensure_data_file()
            return self.load_data()
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{book_id}/return")
async def return_book(
    book_id: str,
    return_data: BorrowRequest,
    service: LibraryService = Depends(get_library_service)
):
    """Return a book"""
    try:
        if service.return_book(book_id, return_data.member_id):
            return {"message": "Book returned successfully"}
        else:
            raise HTTPException(status_code=400, detail="Failed to return book")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: str,
    book_data: BookUpdate,
    service: LibraryService = Depends(get_library_service)
):
    """Update book information"""
    try:
        update_dict = book_data.dict(exclude_unset=True)
        book = service.update_book(book_id, **update_dict)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return BookResponse(**book.to_dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
