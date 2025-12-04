# test-ncpa-api-endpoints
Python tests to check the API endpoints are working as expected on NCPA clients

## How to run the tests
`cd test-ncpa-api-endpoints/`

### Setup the python venv (only needs to be done the first time to set everything up)
`./setup_venv.sh`

### Activate the venv (needs to be run everytime you wish to run the tests)
` source test_ncpa_venv/bin/activate`

### Run tests without logging
`pytest`

### Run tests with logging
`pytest --log-cli-level=INFO`

### Deactivate venv when done
`deactivate`
