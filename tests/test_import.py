import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.import_api import ImportAPI

@pytest.fixture
def api():
    base_url = "https://jsonplaceholder.typicode.com"
    return ImportAPI(base_url)

@pytest.mark.parametrize("user_id", [1])
def test_import_happy_path(api, user_id):
    response = api.import_user(user_id)
    print("Happy Path:", response.json())
    assert response.status_code == 201
    assert response.json()["userId"] == user_id

@pytest.mark.parametrize("user_id", ["invalid", None])
def test_import_sad_path(api, user_id):
    response = api.import_user(user_id)
    print("Sad Path:", response.json())
    assert response.status_code in [201, 400]
