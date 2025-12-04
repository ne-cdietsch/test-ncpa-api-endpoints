import requests
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning
from ncpa_config import *


# Test CPU endpoint
def test_cpu_endpoint():
    url = f"{BASE_URL}/api/cpu?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_cpu_percent_endpoint():
    url = f"{BASE_URL}/api/cpu/percent?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_cpu_percent_as_check_endpoint():
    url = f"{BASE_URL}/api/cpu/percent?token={API_TOKEN}&warning=80&critical=90&check=true"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["returncode"], int)
    assert isinstance(response.json()["stdout"], str)
