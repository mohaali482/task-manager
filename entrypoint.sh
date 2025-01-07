#!/bin/sh

/opt/venv/bin/python manage.py migrate --no-input
/opt/venv/bin/python manage.py collectstatic --no-input

/opt/venv/bin/gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000