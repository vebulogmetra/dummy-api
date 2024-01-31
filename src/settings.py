from pathlib import Path
import os

BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
INIT_DB_SCRIPT = "initdb.sh"

DB_PRODUCTS_TABLENAME = "products"
DB_CATEGORIES_TABLENAME = "categories"

FETCH_CATEGORIES = False
INIT_DB = False
SQLITE_DB_NAME = "dummy-api.db"

POSTGRES_DB = ""
POSTGRES_USER = ""
POSTGRES_PASSWORD = ""
POSTGRES_HOST = ""
POSTGRES_PORT = 5432

BASE_URL = "https://dummyjson.com/"
PRODUCTS_URL = "https://dummyjson.com/products/"
CATEGORIES_URL = "https://dummyjson.com/products/categories/"
