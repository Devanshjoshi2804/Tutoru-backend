#!/bin/bash
python -m pip install -r new_requirements.txt
python manage.py collectstatic --noinput --clear
