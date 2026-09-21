
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from Docker CI/CD!"
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_hello():
    response = client.get("/hello/Hemil")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Hemil!"}