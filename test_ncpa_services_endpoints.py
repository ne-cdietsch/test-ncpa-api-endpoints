import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test services endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("services"),
]

ENDPOINT_DATA_FILTERED = [
    ("services", "&services=ncpa&match=search"),
]

# List of endpoints to test as checks
CHECK_DATA_FILTERED = [
    ("services", "&services=ncpa&match=search"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_services_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint,filters", ENDPOINT_DATA_FILTERED)
def test_services_endpoints_filtered(endpoint, filters):
    get_endpoint_filtered(endpoint, filters)

@pytest.mark.parametrize("endpoint,filters", CHECK_DATA_FILTERED)
def test_services_endpoints_as_checks_filtered(endpoint, filters):
    get_endpoint_as_check_filtered(endpoint, filters)