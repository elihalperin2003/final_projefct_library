from database.db_connection import db_connection as conn


class BookDB:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor
        self.fields = "title, author, genre, is_available, borrowed_by_member_id"

    def create_book(self, data: dict):
        values = tuple(v for v in data.values())
        sql_txt = f"INSERT INTO books ({self.fields})"
        sql_txt += "VALUES (%s, %s, %s, %s, %s)"
        with self.cursor(dictionary=True) as cursor:
            cursor.execute((sql_txt), (values))
        self.conn.commit()

    def get_all_books(self):
        with self.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM books")
            data = cursor.fetchall()
        return data

    def get_book_by_id(self, id: int):
        with self.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
            data = cursor.fetchall()
        return data

    def update_book(self, id: int, data: dict):
        values = tuple(v for v in data.values()) + (id,)
        sql_txt = """
                    UPDATE books
                    SET title = %s, author = %s, genre = %s, is_available = %s, borrowed_by_member_id = %s
                    WHERE id = %s
                      """
        with self.cursor() as cursor:
            cursor.execute(sql_txt, values)
            self.conn.commit()
        print(200)

    def set_availabla(self, id: int, val: bool, member_id: int):
        with self.cursor() as cursor:
            cursor.execute(
                """
                UPDATE books
                SET is_available = %s, borrowed_by_member_id = %s
                WHERE id = %s""",
                (val, member_id, id),
            )
            self.conn.commit()


book_db = BookDB(conn)
