import requests
import pytest
import logging


# Configuration variables for NCPA API tests
logger = logging.getLogger(__name__)
BASE_URL = 'https://localhost:5693/api/'
API_TOKEN = 'mytoken'
SYSTEM_TYPE = 'linux'  # or 'windows', 'macos', 'solaris'
NETWORK_INTERFACE = 'eth0' if SYSTEM_TYPE != 'windows' else 'Ethernet'

# Helper functions to get endpoints
def get_endpoint(endpoint_path):
    url = f"{BASE_URL}/{endpoint_path}?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "error" not in response.json()

def get_endpoint_filtered(endpoint_path, filters):
    url = f"{BASE_URL}/{endpoint_path}?token={API_TOKEN}{filters}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "error" not in response.json()

def get_endpoint_as_check(endpoint_path):
    url = f"{BASE_URL}/{endpoint_path}?token={API_TOKEN}&warning=80&critical=90&check=true"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "error" not in response.json()
    assert isinstance(response.json()["returncode"], int)
    assert isinstance(response.json()["stdout"], str)
    assert "does not exist" not in response.json()["stdout"]

def get_endpoint_as_check_filtered(endpoint_path, filters):
    url = f"{BASE_URL}/{endpoint_path}?token={API_TOKEN}&warning=80&critical=90&check=true{filters}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "error" not in response.json()
    assert isinstance(response.json()["returncode"], int)
    assert isinstance(response.json()["stdout"], str)
    assert "does not exist" not in response.json()["stdout"]