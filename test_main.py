from fastapi.testclient import TestClient

from main import *

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_jokes():
    response = client.get("/jokes")
    assert response.status_code == 200
    assert response.json() == data

def test_random_jokes():
    response = client.get("/jokes/random")
    assert response.status_code == 200
    assert response.json() == randomjoke
