from src.DTOs import ProductDTO, CategoryDTO
from src.external.products import get_products
from src.external.categories import get_categories
from src.storages.crud import SqliteCRUD
from src.utils import initdb
from typing import Iterable
from src.settings import (
    INIT_DB,
    FETCH_CATEGORIES,
    SQLITE_DB_NAME,
    DB_CATEGORIES_TABLENAME,
    DB_PRODUCTS_TABLENAME,
)

db_crud = SqliteCRUD(db_file=SQLITE_DB_NAME)

if INIT_DB:
    initdb()

if FETCH_CATEGORIES:
    categories_from_api: Iterable[CategoryDTO] = get_categories()

    for category in categories_from_api:
        db_crud.insert_entity(table_name=DB_CATEGORIES_TABLENAME, entity_data=category)


products_from_api: Iterable[ProductDTO] = get_products(limit=50, skip=0)


for product in products_from_api:
    category_name: str = product.category
    product.category = None
    product.category_id = db_crud.get_entity(
        table_name=DB_CATEGORIES_TABLENAME,
        entity_field="name",
        entity_value=category_name,
    )[0][0]
    db_crud.insert_entity(table_name=DB_PRODUCTS_TABLENAME, entity_data=product)

products_from_db = db_crud.get_entities(table_name=DB_PRODUCTS_TABLENAME)

db_crud.close_connection()

print("*" * 30)
print(f"DB PRODS: {products_from_db}")
print("*" * 30)
