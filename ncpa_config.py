import requests
import pytest
import logging

logger = logging.getLogger(__name__)
BASE_URL = 'https://localhost:5693'
API_TOKEN = 'mytoken'
SYSTEM_TYPE = 'linux'  # or 'windows', 'macos', 'solaris'

@pytest.fixture
def test_api_endpoint(endpoint):
    url = f"{BASE_URL}/{endpoint}?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
