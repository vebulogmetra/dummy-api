from src.settings import CATEGORIES_URL
from src.external.api_client import APIClient
from src.DTOs import CategoryDTO
from typing import Iterable

api_client = APIClient()


def get_categories() -> Iterable[CategoryDTO]:
    response = api_client.get(url=CATEGORIES_URL)
    response_raw: list[str] = response.json()
    categories: set[CategoryDTO] = {CategoryDTO(name=c) for c in response_raw}
    return categories
