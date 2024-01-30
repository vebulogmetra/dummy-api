#!/bin/bash

# Параметры подключения к базе данных SQLite
DB_FILE="../../dammy-api.db"
SQL_FILE="./create_tables.sql"

if [ ! -f "$DB_FILE" ]; then
    echo "База данных $DB_FILE не существует. Создание новой базы данных..."
    touch "$DB_FILE"
    sqlite3 "$DB_FILE" < "$SQL_FILE"
    echo "База данных и таблицы успешно созданы."
else
    echo "База данных $DB_FILE уже существует. Пропуск."
fi