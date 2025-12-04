import requests
import pytest
import logging
from urllib3.exceptions import InsecureRequestWarning
from ncpa_config import *


# Test Disk endpoint
def test_disk_endpoint():
    url = f"{BASE_URL}/api/disk?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_disk_physical():
    url = f"{BASE_URL}/api/disk/physical?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_disk_mount():
    url = f"{BASE_URL}/api/disk/mount?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# The logical device names will vary based on OS and configuration
if SYSTEM_TYPE != 'windows':
    def test_disk_logical_root_used_percent():
        url = f"{BASE_URL}/api/disk/logical/|/used_percent?token={API_TOKEN}"
        response = requests.get(url, verify=False)
        logger.info(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_disk_logical_root_used_percent_as_check():
        url = f"{BASE_URL}/api/disk/logical/|/used_percent?token={API_TOKEN}&warning=80&critical=90&check=true"
        response = requests.get(url, verify=False)
        logger.info(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
else:
    def test_disk_logical_c_used_percent():
        url = f"{BASE_URL}/api/disk/logical/C:|/used_percent?token={API_TOKEN}"
        response = requests.get(url, verify=False)
        logger.info(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_disk_logical_c_used_percent_as_check():
        url = f"{BASE_URL}/api/disk/logical/C:|/used_percent?token={API_TOKEN}&warning=80&critical=90&check=true"
        response = requests.get(url, verify=False)
        logger.info(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
