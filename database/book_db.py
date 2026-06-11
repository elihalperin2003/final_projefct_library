from database.db_connection import db_connection as conn

class BookDB:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor(dictionary=True)
    
    def create_book(self):
        pass

    def get_all_books(self):
        with self.cursor as cursor:
            cursor.execute(
                "SELECT * FROM books"
            )
            data = cursor.fetchall()
        self.conn.close()
        return data
    
book_db = BookDB()