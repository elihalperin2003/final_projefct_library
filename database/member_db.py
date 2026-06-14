from database.db_connection import db_connection as conn


class MemberDB:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor
        self.fields = "name, email, is_active, total_borrows"

    def create_member(self, data: dict):
        txt_qsl = f"INSERT INTO members ({self.fields})"
        txt_qsl += "VALUES (%s, %s, %s, %s)"
        with self.cursor() as cur:
            cur.execute(txt_qsl, tuple(v for v in data.values()))
        self.conn.commit()

    def get_all_members(self):
        with self.cursor() as cur:
            cur.execute("SELECT * FROM members")
            result = cur.fetchall()
        return result

    def get_book_by_id(self, id: int):
        with self.cursor() as cur:
            cur.execute("SELECT * FROM members WHERE id = %s", (id,))
            data = cur.fetchall()
        return data

    def update_book(self, id: int, data: dict):
        values = tuple(val for val in data.values())
        sql_txt = """
        UPDATE members
        SET name = %s, email = %s, is_active = %s, total_borrows = %s
        WHERE id = %s
        """
        with self.cursor() as cur:
            cur.execute(sql_txt, (*values, id))
        self.conn.commit()
        print(201)


member_db = MemberDB(conn)
