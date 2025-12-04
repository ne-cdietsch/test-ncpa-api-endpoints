#!/bin/bash

python3 -m venv test_ncpa_venv
source test_ncpa_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt