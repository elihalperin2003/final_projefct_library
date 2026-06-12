from database.db_connection import create_tables
from database.db_connection import db_connection as conn
from database.book_db import book_db


def main():
    create_tables(conn)
    book_db.update_book(9, {"title": "hg", "author": "sk", "genre": "Fiction", "is_available": True, "borrowed_by_member_id": 9})
    print(*book_db.get_book_by_id(9))


main()
