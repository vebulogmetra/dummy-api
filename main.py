from src.DTOs import ProductDTO, CategoryDTO
from src.external.products import get_products
from src.external.categories import get_categories
from src.storages.manager import DatabaseManager
from src.storages.crud import insert_category, insert_product
from src.utils import initdb
from typing import Iterable
from src.settings import (
    INIT_DB,
    SQLITE_DB_NAME,
    DB_TYPE_SQLITE,
    DB_CATEGORIES_TABLENAME,
    DB_PRODUCTS_TABLENAME,
)

if INIT_DB:
    initdb()

sqlite_manager = DatabaseManager(db_type=DB_TYPE_SQLITE, database=SQLITE_DB_NAME)
sqlite_manager.connect()


def get_categories_from_external_api() -> Iterable[CategoryDTO]:
    categories: Iterable[CategoryDTO] = get_categories()
    return categories


def get_products_from_external_api(limit=5, skip=0) -> Iterable[ProductDTO]:
    products: Iterable[ProductDTO] = get_products(limit=limit, skip=skip)
    return products


def save_to_db(table_name: str, entitys: Iterable[CategoryDTO] | Iterable[ProductDTO]):
    results = []
    if table_name == DB_CATEGORIES_TABLENAME:
        for category in entitys:
            r = insert_category(db_manager=sqlite_manager, category_data=category)
            results.append(r)

    elif table_name == DB_PRODUCTS_TABLENAME:
        for product in entitys:
            r = insert_product(db_manager=sqlite_manager, product_data=product)
            results.append(r)
    return results


if __name__ == "__main__":
    categories = get_categories_from_external_api()
    products = get_products_from_external_api()
    print(f"products: {products}")
    save_res_cats = save_to_db(table_name=DB_CATEGORIES_TABLENAME, entitys=categories)
    # save_res_prods = save_to_db(table_name=DB_PRODUCTS_TABLENAME, entitys=products)

    print("*" * 30)
    print(f"RES CATS: {save_res_cats}")
    # print(f"RES PRODS: {save_res_prods}")
    print("*" * 30)

    sqlite_manager.close()
