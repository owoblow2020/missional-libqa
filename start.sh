#!/bin/bash

pip install -e .
python manage.py migrate  --no-input
python manage.py createcachetable
python manage.py runserver 0.0.0.0:8000
