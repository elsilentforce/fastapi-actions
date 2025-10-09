from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# This is a comment
def test_index():
    response = client.get("/items/")
    assert response.status_code == 200
