from src.settings import CATEGORIES_URL
from src.api_client import APIClient
from typing import Iterable

api_client = APIClient()


def get_categories() -> Iterable[str]:
    response = api_client.get(url=CATEGORIES_URL)
    categories: tuple[str] = tuple(response.json())
    return categories
