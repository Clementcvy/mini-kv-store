from fastapi.testclient import TestClient

from kvstore.main import app

client = TestClient(app)


def test_health_return_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
