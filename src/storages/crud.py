from src.DTOs import ProductDTO, CategoryDTO
from src.storages.manager import DatabaseManager
from typing import Iterable


def insert_product(db_manager: DatabaseManager, product_data: ProductDTO):
    query = """INSERT INTO products (product_id, title, description, price, thumbnail, category_id)
               VALUES (:product_id, :title, :description, :price, :thumbnail, :category_id)
               RETURNING product_id"""
    result = db_manager.execute_query(query, product_data.to_dict())
    return result[0]


def select_product(
    db_manager: DatabaseManager, by_field: str, by_value: str | int | float
):
    query = """SELECT * FROM products WHERE :by_field = :by_value"""
    values = {"by_field": by_field, "by_value": by_value}
    result = db_manager.execute_query(query, values)
    return result[0]


def delete_product(
    db_manager: DatabaseManager, by_field: str, by_value: str | int | float
):
    query = """DELETE FROM products WHERE :by_field = :by_value RETURNING product_id"""
    values = {"by_field": by_field, "by_value": by_value}
    result = db_manager.execute_query(query, values)
    return result[0]


def insert_category(db_manager: DatabaseManager, category_data: CategoryDTO):
    query = """INSERT INTO categories (name) VALUES (:name) RETURNING category_id"""
    values = {"name": category_data.name}
    result = db_manager.execute_query(query, values)
    return result[0]


def select_category(
    db_manager: DatabaseManager, by_field: str, by_value: str | int | float
):
    query = """SELECT * FROM categories WHERE :by_field = :by_value"""
    values = {"by_field": by_field, "by_value": by_value}
    result = db_manager.execute_query(query, values)
    return result[0]


def delete_category(
    db_manager: DatabaseManager, by_field: str, by_value: str | int | float
):
    query = """DELETE FROM categories WHERE :by_field = :by_value RETURNING category_id"""
    values = {"by_field": by_field, "by_value": by_value}
    result = db_manager.execute_query(query, values)
    return result[0]


# postgres_manager = DatabaseManager(
#     db_type=DB_TYPE_POSTGRES,
#     database=POSTGRES_DB,
#     user=POSTGRES_USER,
#     password=POSTGRES_PASSWORD,
#     host=POSTGRES_HOST,
#     port=POSTGRES_PORT,
# )
# postgres_manager.connect()
# result = postgres_manager.execute_query("SELECT * FROM products")
# print(result)
# postgres_manager.close()
