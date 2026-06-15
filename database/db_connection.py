import mysql.connector


class Connection:
    def __init__(self):
        self.conn = self.get_connection()
        self.create_tables(self.conn)

    def get_connection(self):
        return mysql.connector.connect(host="localhost", user="root", password="root", database="library_db")

    def create_tables(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM ("Fiction", "Non-Fiction", "Science" ,"History", "Other") NOT NULL,
                    is_available BOOLEAN DEFAULT TRUE NOT NULL,
                    borrowed_by_member_id INT 
                )
                """)
            cursor.execute("""CREATE TABLE IF NOT EXISTS members (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(200) UNIQUE NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE NOT NULL,
                    total_borrows INT NOT NULL
                )
                """)


db_connection = Connection()
