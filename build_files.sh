#!/bin/bash

# Install dependencies
python3 -m pip install -r new_requirements.txt

# Run migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput --clear
