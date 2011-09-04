#!/usr/bin/env bash

uwsgi \
    --master \
    --processes 4 \
    --home $VIRTUAL_ENV \
    --chdir $VIRTUAL_ENV/bin \
    --env DJANGO_SETTINGS_MODULE=perfo_analysis.conf.local.settings \
    --http :8084 \
    --module "django.core.handlers.wsgi:WSGIHandler()" \
    --static-map /static=$VIRTUAL_ENV/var/static
