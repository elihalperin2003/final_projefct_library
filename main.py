from database.db_connection import create_tables
from database.db_connection import db_connection as conn

def main():
    create_tables(conn)

main()