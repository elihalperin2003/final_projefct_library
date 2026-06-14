from database.db_connection import create_tables
from database.db_connection import db_connection as conn
from database.book_db import book_db
from database.member_db import member_db


def main():
    create_tables(conn)
    # member_db.create_member({"name": "loopy", "email": "lam@poop", "is_active": True, "total_borrows": 0})
    print(member_db.get_all_members())
    print(member_db.get_book_by_id(1))


main()
