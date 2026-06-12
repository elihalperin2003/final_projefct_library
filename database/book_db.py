from database.db_connection import db_connection as conn


class BookDB:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor
        self.fields = "title, author, genre, is_available, borrowed_by_member_id"

    def create_book(self, data: dict):
        values = tuple(v for v in data.values())
        print(values)
        sql_txt = f"INSERT INTO books ({self.fields})"
        sql_txt += "VALUES (%s, %s, %s, %s, %s)"
        with self.cursor(dictionary=True) as cursor:
            cursor.execute((sql_txt), (values))
        self.conn.commit()
        print(200)

    def get_all_books(self):
        with self.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM books")
            data = cursor.fetchall()
        self.conn.close()
        return data

    def get_book_by_id(self, id: int):
        with self.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
            data = cursor.fetchall()
        self.conn.close()
        return data


book_db = BookDB(conn)
