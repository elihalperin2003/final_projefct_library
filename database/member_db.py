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

    def get_member_by_id(self, id: int):
        with self.cursor() as cur:
            cur.execute("SELECT * FROM members WHERE id = %s", (id,))
            data = cur.fetchall()
        return data

    def update_member(self, id: int, data: dict):
        values = tuple(val for val in data.values())
        sql_txt = """
        UPDATE members
        SET name = %s, email = %s, is_active = %s, total_borrows = %s
        WHERE id = %s
        """
        with self.cursor() as cur:
            cur.execute(sql_txt, (*values, id))
        self.conn.commit()

    def deactivate_member(self, id):
        with self.cursor() as cur:
            cur.execute("UPDATE members SET is_active = FALSE WHERE id = %s", (id,))
        self.conn.commit()

    def activate_member(self, id):
        with self.cursor() as cur:
            cur.execute("UPDATE members SET is_active = TRUE WHERE id = %s", (id,))
        self.conn.commit()

    def increment_borrows(self, id: int):
        with self.cursor() as cur:
            cur.execute("UPDATE members SET total_borrows = total_borrows + 1 WHERE id = %s", (id,))
        self.conn.commit()

    def count_active_members(self):
        with self.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM members WHERE is_active = True")
            data = cur.fetchone()
        return data[0]

    def get_top_member(self):
        with self.cursor() as cur:
            cur.execute("SELECT name FROM members ORDER BY total_borrows DESC limit 1")
            data = cur.fetchone()
        return data[0]


member_db = MemberDB(conn)
