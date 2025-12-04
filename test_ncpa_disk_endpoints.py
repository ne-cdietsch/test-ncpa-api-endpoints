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

def test_disk_physical_endpoint():
    url = f"{BASE_URL}/api/disk/physical?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_disk_mount_endpoint():
    url = f"{BASE_URL}/api/disk/mount?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# The logical device names will vary based on OS and configuration
def test_disk_logical_endpoint():
    url = f"{BASE_URL}/api/disk/logical?token={API_TOKEN}"
    response = requests.get(url, verify=False)
    logger.info(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

