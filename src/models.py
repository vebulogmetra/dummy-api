from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    id: int
    title: str
    description: str
    price: float
    thumbnail: str
    category: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[str] = None
    deleted_reason: Optional[str] = None


@dataclass
class Category:
    id: int
    name: str
    created_at: datetime
