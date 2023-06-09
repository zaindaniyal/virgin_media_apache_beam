#!/bin/bash
# Create a virtual environment
python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate
# Install the required dependencies
pip install -r requirements.txt
# Run the Python files
python main.py
python -m unittest discover -s . -p "*tests.py"
# Deactivate the virtual environment
deactivate