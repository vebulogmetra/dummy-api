from src.settings import PRODUCTS_URL, CATEGORIES_URL
from src.api_client import APIClient
from src.DTOs import Product
from typing import Iterable

api_client = APIClient()


def get_products(
    limit: int = 3,
    skip: int = 0,
    select: Iterable[str] = (
        "id",
        "title",
        "description",
        "price",
        "thumbnail",
        "category",
    ),
) -> Iterable[Product]:
    params = {
        "limit": limit,
        "skip": skip,
        "select": select,
    }
    response = api_client.get(url=PRODUCTS_URL, params=params)
    products_raw: list[dict] = response.json().get("products", [])
    products: list[Product] = [Product.from_dict(json_data) for json_data in products_raw]
    return products
