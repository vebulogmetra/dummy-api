from datetime import datetime
from typing import Optional


class Product:
    def __init__(self):
        self.product_id: int = 0
        self.title: str = ""
        self.description: str = ""
        self.price: float = 0
        self.thumbnail: str = ""
        self.category_id: int = ""
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.is_deleted: bool = False
        self.deleted_at: Optional[datetime] = None
        self.deleted_by: Optional[str] = None
        self.deleted_reason: Optional[str] = None

    def to_dict(self, from_db: bool = False) -> dict:
        _d = {
            "product_id": self.product_id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "thumbnail": self.thumbnail,
            "category_id": self.category_id,
        }

        if from_db:
            _d1 = {
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "is_deleted": self.is_deleted,
                "deleted_at": self.deleted_at,
                "deleted_by": self.deleted_by,
                "deleted_reason": self.deleted_reason,
            }
            _d = _d | _d1
        return _d


class Category:
    def __init__(self) -> None:
        self.category_id: int = 0
        self.name: str = ""
        self.created_at: datetime = datetime.now()

    def to_dict(self, from_db: bool = False) -> dict:
        _d = {
            "category_id": self.category_id,
            "name": self.name,
        }

        if from_db:
            _d1 = {
                "created_at": self.created_at,
            }
            _d = _d | _d1
        return _d
