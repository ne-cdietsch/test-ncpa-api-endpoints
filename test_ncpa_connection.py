import requests
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning
from ncpa_config import *


# Test we can connect to the API
def test_connection():
    url = f"{BASE_URL}/testconnect?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert response.json()["value"] == "Success."

def test_api():
    url = f"{BASE_URL}/api?token={API_TOKEN}"
    test_api_endpoint(url)
