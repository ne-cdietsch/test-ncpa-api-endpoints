import requests
import pytest
import logging

logger = logging.getLogger(__name__)
BASE_URL = 'https://localhost:5693'
API_TOKEN = 'mytoken'
SYSTEM_TYPE = 'linux'  # or 'windows', 'macos', 'solaris'

def get_endpoint(endpoint_path):
    url = f"{BASE_URL}/{endpoint_path}?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

