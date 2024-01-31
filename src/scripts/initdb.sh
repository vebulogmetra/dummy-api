#!/bin/bash

# Получение полного пути к файлам
BASEDIR=$(dirname "$0")
DB_FILE="dummy-api.db"
SQL_FILE="$BASEDIR/create_tables.sql"

DB_FILE_PATH=$(realpath "$DB_FILE")
SQL_FILE_PATH=$(realpath "$SQL_FILE")
echo "[DB FILE PATH] = $DB_FILE_PATH"
echo "[SQL_FILE_PATH] = $SQL_FILE_PATH"

if [ ! -f "$DB_FILE" ]; then
    echo "[=>]База данных $DB_FILE не существует. Создание новой базы данных..."
    touch "$DB_FILE"
    echo "[=>]Создание таблиц..."
    sqlite3 "$DB_FILE" < "$SQL_FILE"
    echo "[+]База данных и таблицы успешно созданы."
else
    echo "[-]База данных $DB_FILE уже существует. Пропуск."
    echo "[=>]Создание таблиц..."
    sqlite3 "$DB_FILE" < "$SQL_FILE"
    echo "[+]Таблицы успешно созданы."
fi