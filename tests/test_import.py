import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.import_api import ImportAPI

@pytest.fixture
def api():
    base_url = "https://api.test.worldsys.ar"
    token = "xxx"  # ⚠️ Reemplazar por el token real
    return ImportAPI(base_url, token)

@pytest.mark.parametrize("person_id", [111])
def test_import_happy_path(api, person_id):
    response = api.import_person(person_id)
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200

@pytest.mark.parametrize("person_id", ["invalid", None])
def test_import_sad_path(api, person_id):
    response = api.import_person(person_id)
    print(f"Sad Path Response: {response.text}")
    assert response.status_code in [400, 422]
