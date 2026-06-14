from database.db_connection import create_tables
from database.db_connection import db_connection as conn
from database.book_db import book_db


def main():
    create_tables(conn)
    print(book_db.count_available_books())


main()
