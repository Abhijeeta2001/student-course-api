from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post("/students/", json={"name": "Bob", "email": "bob@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Bob"
