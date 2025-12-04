import requests
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning
from ncpa_config import *


# Test we can connect to the API
def test_connection():
    url = f"{BASE_URL}/testconnect?token={api_token}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert response.json()["value"] == "Success."

def test_api():
    url = f"{BASE_URL}/api?token={api_token}"
    response = requests.get(url, verify=False)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
