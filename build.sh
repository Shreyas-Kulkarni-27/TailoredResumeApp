#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip, setuptools, and wheel
python -m pip install --upgrade pip setuptools wheel

# Install project dependencies
pip install -r requirements.txt

# Add any other build steps you need
