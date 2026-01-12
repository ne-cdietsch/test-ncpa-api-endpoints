import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test interface endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("interface"),
    ("interface/{interface}").format(interface=NETWORK_INTERFACE),
    ("interface/{interface}/bytes_recv").format(interface=NETWORK_INTERFACE),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("interface/{interface}/bytes_recv").format(interface=NETWORK_INTERFACE),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_interface_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_interface_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)
