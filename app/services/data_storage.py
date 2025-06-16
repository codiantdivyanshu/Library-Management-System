import json
from pathlib import Path
from typing import Dict, Any

class DataStorage:
    """File-based storage service demonstrating file I/O and error handling"""

    def __init__(self, data_file: str = "data/library_data.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_data_file()

    def _ensure_data_file(self):
        """Create or reset the data file if it doesn't exist or is empty"""
        if not self.data_file.exists() or self.data_file.stat().st_size == 0:
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
            raise RuntimeError(f"Error loading data: {str(e)}")

    def save_data(self, data: Dict[str, Any]):
        """Save data to the JSON file"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving data: {str(e)}")
