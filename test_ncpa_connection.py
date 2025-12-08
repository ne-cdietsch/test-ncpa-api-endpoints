import requests
import pytest
import logging
from ncpa_config import get_endpoint


ENDPOINT_DATA = [
    ("testconnect"),
    ("api"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_api_endpoints(endpoint):
    get_endpoint(endpoint)
