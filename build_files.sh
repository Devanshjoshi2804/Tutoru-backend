#!/bin/bash

# Activate virtual environment
source venv/activate

# Install dependencies
pip install -r new_requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
