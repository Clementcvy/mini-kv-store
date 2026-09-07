"""Execute SQL queries"""


class Repository:
    def __init__(self, conn):
        self.conn = conn

    def set(self, key, value):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO kv_items (key, value) "
                "VALUES (%s, %s) "
                "ON CONFLICT (key) "
                "DO UPDATE SET value=EXCLUDED.value, updated_at=NOW()",
                (key, value),
            )

    def get(self, key):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT key, value, created_at, updated_at FROM kv_items WHERE key=%s",
                (key,),
            )
            return cur.fetchone()

    def delete(self, key):
        with self.conn.cursor() as cur:
            cur.execute(
                "DELETE FROM kv_items WHERE key=%s RETURNING key, value", (key,)
            )
            return cur.fetchone()
