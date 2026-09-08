from fastapi.testclient import TestClient

from kvstore.main import app

client = TestClient(app)


def test_put_then_get():
    key = "cle1"
    value = "valeur1"
    response = client.put(f"/v1/kv/{key}", json={"value": value})
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}
    response = client.get(f"/v1/kv/{key}")
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}


def test_put_two_times():
    key = "cle2"
    value = "valeur2"
    response = client.put(f"/v1/kv/{key}", json={"value": value})
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}
    value = "valeur3"
    response = client.put(f"/v1/kv/{key}", json={"value": value})
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}


def test_get_not_existing_key():
    response = client.get("/v1/kv/doesnt_exist")
    assert response.status_code == 404


def test_delete():
    key = "cle3"
    value = "valeur4"
    response = client.put(f"/v1/kv/{key}", json={"value": value})
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}
    response = client.delete(f"/v1/kv/{key}")
    assert response.status_code == 204
    response = client.get(f"/v1/kv/{key}")
    assert response.status_code == 404


def test_delete_not_existing_key():
    response = client.delete("/v1/kv/doesnt_exist")
    assert response.status_code == 404
