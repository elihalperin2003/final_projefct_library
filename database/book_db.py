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

    def count_total_books(self):
        with self.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM books
                """)
            data = cursor.fetchall()
        return data

    def count_available_books(self):
        with self.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM books
                WHERE is_available = True
                """)
            data = cursor.fetchall()
        return data

    def count_borrowed_books(self):
        with self.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM books
                WHERE is_available = False
                """)
            data = cursor.fetchall()
        return data

    def count_by_genre(self, genre):
        with self.cursor() as cur:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM books
                WHERE genre = %s
                """,
                (genre,),
            )
            result = cur.fetchall()
        return result

    def count_active_borrows_by_member(self, member_id):
        with self.cursor() as cur:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM books
                WHERE borrowed_by_member_id = %s
                """,
                (member_id,),
            )
            result = cur.fetchall()
        return result


book_db = BookDB(conn)
