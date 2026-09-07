from kvstore.repository import Repository
from kvstore.db import get_connection


def test_queries():
    conn = get_connection()
    repo = Repository(conn)
    key = "cle1"
    value = "valeur1"
    repo.set(key, value)
    _, read_value, _, _ = repo.get(key)
    assert read_value == "valeur1"
    value2 = "valeur2"
    repo.set(key, value2)
    _, read_value, _, _ = repo.get(key)
    assert read_value == "valeur2"
    repo.delete(key)
    assert repo.get(key) is None
    conn.close()
