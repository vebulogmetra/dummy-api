from src.settings import PRODUCTS_URL, CATEGORIES_URL
from src.external.api_client import APIClient
from src.DTOs import ProductDTO
from typing import Iterable

api_client = APIClient()


def get_products(
    limit: int = 3,
    skip: int = 0,
    select: Iterable[str] = (
        "title",
        "description",
        "price",
        "thumbnail",
        "category",
    ),
) -> Iterable[ProductDTO]:
    params = {
        "limit": limit,
        "skip": skip,
        "select": select,
    }
    response = api_client.get(url=PRODUCTS_URL, params=params)
    products_raw: list[dict] = response.json().get("products", [])
    products: list[ProductDTO] = [
        ProductDTO.from_dict(json_data) for json_data in products_raw
    ]
    return products
