from src.products import Product, get_products
from src.categories import get_categories


categories: tuple[str] = get_categories()
products: list[Product] = get_products(limit=5, skip=0)
