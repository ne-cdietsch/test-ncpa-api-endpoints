import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test Disk endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("disk"),
    ("disk/physical"),
    ("disk/mount"),
    ("disk/logical"),
    ("disk/logical/|/used_percent") if SYSTEM_TYPE != 'windows' else ("disk/logical/C:|/used_percent"),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("disk/logical/|/used_percent") if SYSTEM_TYPE != 'windows' else ("disk/logical/C:|/used_percent"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_disk_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_disk_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)
