import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test interface endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("interface"),
    ("interface/eth0") if SYSTEM_TYPE != 'windows' else ("interface/Ethernet"),
    ("interface/eth0/bytes_recv") if SYSTEM_TYPE != 'windows' else ("interface/Ethernet/bytes_recv"),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("interface/eth0/bytes_recv") if SYSTEM_TYPE != 'windows' else ("interface/Ethernet/bytes_recv"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_interface_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_interface_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)
