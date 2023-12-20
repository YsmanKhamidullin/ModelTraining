import json
import os.path

from fastapi.testclient import TestClient
from app.api.fastapi_app import app

client = TestClient(app)


def test_create_item():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "data/expected_results.json")) as json_file:
        expected_results = json.load(json_file)
        url = "/ocr_image/"
        for item in expected_results:
            file_path = os.path.join(dir_path, "data/images", item['filename'])
            response = client.post(url, files={"file": ("filename", open(file_path, "rb"), item['filename'])})
            assert response.status_code == 200
            assert response.json()["text"] == item['result']
