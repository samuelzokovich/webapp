from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    quantity: int
    category: str
    tags: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str  # Blob name as ID

    class Config:
        from_attributes = True
