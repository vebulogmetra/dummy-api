PRAGMA foreign_keys=OFF;

CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    title VARCHAR,
    description VARCHAR,
    price REAL,
    thumbnail TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT false,
    deleted_at TIMESTAMP NULL,
    deleted_reason TEXT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
