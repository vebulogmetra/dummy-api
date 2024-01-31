from src.DTOs import ProductDTO, CategoryDTO
from sqlite3 import Connection
import sqlite3
from typing import TypeVar
from contextlib import closing


EntityDTO = TypeVar("EntityDTO", ProductDTO, CategoryDTO)


class SqliteCRUD:
    def __init__(self, db_file: str):
        self.conn: Connection = sqlite3.connect(db_file)

    def insert_entity(self, table_name: str, entity_data: EntityDTO):
        _entity_data: dict = entity_data.to_dict()
        columns = ", ".join(_entity_data.keys())
        placeholders = ", ".join(":" + key for key in _entity_data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self._execute_query(query, _entity_data)

    def get_entities(self, table_name: str):
        query = f"SELECT * FROM {table_name}"
        return self._execute_query(query)

    def get_entity(self, table_name: str, entity_field: str, entity_value: int | str):
        query = f"SELECT * FROM {table_name} WHERE {entity_field} = :entity_value"
        return self._execute_query(query, {"entity_value": entity_value})

    def delete_entity(self, table_name: str, entity_id: int):
        query = f"DELETE FROM {table_name} WHERE id = :entity_id"
        self._execute_query(query, {"entity_id": entity_id})

    def _execute_query(self, query, values=None):
        with closing(self.conn.cursor()) as cursor:
            try:
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

            except Exception as e:
                print(f"[x] Sqlite execute query failed. Rollback...: {e}")
                self.conn.rollback()
                raise e

    def close_connection(self):
        if self.conn:
            try:
                self.conn.commit()
            except Exception as e:
                print(f"[x] Sqlite commit failed: {e}")
            finally:
                self.conn.close()
