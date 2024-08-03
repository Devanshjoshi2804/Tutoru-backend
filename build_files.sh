#!/bin/bash

# Use the virtual environment's pip
venv/bin/python -m pip install -r new_requirements.txt

# Run migrations
venv/bin/python manage.py migrate

# Collect static files
venv/bin/python manage.py collectstatic --noinput
