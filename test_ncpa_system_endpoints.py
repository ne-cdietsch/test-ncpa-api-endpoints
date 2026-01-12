import pytest
# Import ncpa_config module to access configuration and helper functions
from ncpa_config import *


# Test system endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("system"),
    ("system/node"),
    ("system/agent_version"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_system_endpoints(endpoint):
    get_endpoint(endpoint)
