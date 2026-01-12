import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test processes endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("processes"),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("processes"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_processes_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_processes_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)

# Additional filter configurations
FILTERS = [
    "&name=ncpa",
    "&match=search"
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_processes_endpoints_filtered(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_processes_endpoints_as_checks_filtered(endpoint):
    get_endpoint_as_check(endpoint)