#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/profiles-api'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

git pull
$VIRTUALENV_BASE_PATH/profiles-api/bin/python3 manage.py migrate
$VIRTUALENV_BASE_PATH/profiles-api/bin/python3 manage.py collectstatic --noinput
supervisorctl restart profiles_api

echo "DONE! :)"
