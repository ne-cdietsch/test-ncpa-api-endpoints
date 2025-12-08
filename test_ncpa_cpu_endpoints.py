import requests
import pytest
import logging
from ncpa_config import *


# Test CPU endpoint
ENDPOINT_DATA = [
    ("cpu"),
    ("cpu/percent"),
]

CHECK_DATA = [
    ("cpu/percent"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_cpu_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_cpu_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)

