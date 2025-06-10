from abc import ABC, abstractmethod 
from datetime import datetime
from typing import Optional 
import uuid 

class BaseEntity (ABC):
  """Abstract base class for all entities"""

  def __init__(self,name:, str):
    self._id: str(uuid.uuid4())
    self._created_at: datetime = datetime.now()
    self._updated_at: datetime = datetime.now()

  @property 
  def id(self) -> str:
    return self._id 
