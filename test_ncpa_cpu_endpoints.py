import requests
import pytest
import logging
from ncpa_config import *


# Test CPU endpoint
ENDPOINT_DATA = [
    ("cpu"),
    ("cpu/percent"),
    ("cpu/percent&warning=80&critical=90&check=true"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_cpu_endpoints(endpoint):
    get_endpoint(endpoint)
