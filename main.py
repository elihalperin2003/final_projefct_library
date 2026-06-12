from database.db_connection import create_tables
from database.db_connection import db_connection as conn
from database.book_db import book_db


def main():
    create_tables(conn)
    # book_db.create_book({"title": "hp", "author": "jkr", "genre": "Fiction", "is_available": True, "borrowed_by_member_id": 5})
    # print(*book_db.get_all_books())
    print(book_db.get_book_by_id(5))


main()
