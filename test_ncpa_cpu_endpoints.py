from ncpa_config import get_endpoint, get_endpoint_as_check


# Test CPU endpoint
#
# List of endpoints to test
ENDPOINT_DATA = [
    ("cpu"),
    ("cpu/percent"),
]

# List of endpoints to test as checks
CHECK_DATA = [
    ("cpu/percent"),
]

@pytest.mark.parametrize("endpoint", ENDPOINT_DATA)
def test_cpu_endpoints(endpoint):
    get_endpoint(endpoint)

@pytest.mark.parametrize("endpoint", CHECK_DATA)
def test_cpu_endpoints_as_checks(endpoint):
    get_endpoint_as_check(endpoint)

