from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: str
    price: float
    thumbnail: str
    category: str


class Category(BaseModel):
    name: str
