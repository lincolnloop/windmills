#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=perfo_analysis.conf.local.settings

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"

cd "$SCRIPT_DIR/../.."

uwsgi --home $VIRTUAL_ENV \
    --http :8084 \
    --master \
    --processes 4 \
    --module "django.core.handlers.wsgi:WSGIHandler()" \
    --static-map /static=$VIRTUAL_ENV/var/static
