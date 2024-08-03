#!/bin/bash

# Install dependencies
python -m pip install -r new_requirements.txt

# Run migrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput --clear
