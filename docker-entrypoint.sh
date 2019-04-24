#!/bin/sh

echo "start to migrate database"

/venv/bin/python manage.py makemigrations photo person album
/venv/bin/python manage.py migrate

exec "$@"
