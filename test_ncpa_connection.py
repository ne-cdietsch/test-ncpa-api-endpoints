import requests
import pytest
import logging
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test NCPA connection and basic API endpoint functionality 
#
# List of endpoints to test
ENDPOINT_DATA = [
    (""),
]

def test_connection():
    url = f"{BASE_URL.replace("api/", "")}/testconnect?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert response.json()["value"] == "Success."

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_api_endpoints(endpoint):
    get_endpoint(endpoint)
