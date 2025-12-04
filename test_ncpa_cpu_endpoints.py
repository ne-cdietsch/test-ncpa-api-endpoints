import requests
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning

logger = logging.getLogger(__name__)

BASE_URL = 'https://192.168.166.200:5693'
api_token = 'mytoken'

# Test CPU endpoint
def test_cpu_endpoint():
    url = f"{BASE_URL}/api/cpu?token={api_token}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_cpu_percent_endpoint():
    url = f"{BASE_URL}/api/cpu/percent?token={api_token}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_cpu_percent_as_check_endpoint():
    url = f"{BASE_URL}/api/cpu/percent?token={api_token}&warning=80&critical=90&check=true"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["returncode"], int)
    assert isinstance(response.json()["stdout"], str)
    