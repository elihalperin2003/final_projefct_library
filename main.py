from database.db_connection import create_tables
from database.db_connection import db_connection as conn
from database.book_db import book_db
from database.member_db import member_db


def main():
    create_tables(conn)
    # member_db.create_member({"name": "mishel", "email": "mishel@poop", "is_active": True, "total_borrows": 3})
    # member_db.update_book(1, {"name": "loopy_abu", "email": "la@poop", "is_active": True, "total_borrows": 2})
    # print(member_db.get_all_members())
    print(member_db.get_top_member())


main()
