import sqlite3
import psycopg2


class DatabaseManager:
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        self.connection = None
        if self.db_type == "sqlite":
            self.database = kwargs.get("database")
        elif self.db_type == "postgres":
            self.database = kwargs.get("database")
            self.user = kwargs.get("user")
            self.password = kwargs.get("password")
            self.host = kwargs.get("host")
            self.port = kwargs.get("port")

    def connect(self):
        if self.db_type == "sqlite":
            self.connection = sqlite3.connect(self.database)
        elif self.db_type == "postgres":
            self.connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def execute_query(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        self.connection.close()
