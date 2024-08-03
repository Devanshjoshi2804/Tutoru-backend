#!/bin/bash
python3 -m pip install -r new_requirements.txt
python3 manage.py collectstatic --noinput --clear
