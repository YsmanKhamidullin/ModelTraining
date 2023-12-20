from fastapi.testclient import TestClient
from app.api.fastapi_app import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/ocr_image/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
