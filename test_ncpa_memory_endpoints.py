import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test memory endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("memory"),
    ("memory/virtual"),
    ("memory/virtual/used"),
    ("memory/swap"),
    ("memory/swap/used"),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("memory/virtual/used"),
    ("memory/swap/used"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_memory_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_memory_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)
