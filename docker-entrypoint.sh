#!/bin/bash

set -e


if [[ "$WAIT_FOR_IT_ADDRESS" ]]; then
    wait-for-it.sh $WAIT_FOR_IT_ADDRESS --timeout=30
fi


if [[ "$APPLY_MIGRATIONS" = "true" ]]; then
    ./manage.py migrate --noinput
fi


if [[ "$CREATE_SUPERUSER" = "true" ]]; then
    ./manage.py create_admin_superuser
fi

if [[ "$HELSINKI_ACTIVITIES_TEST_DATA" = "true" ]]; then
    ./manage.py helsinki_activities_test_data
fi

if [[ "$TESTING" = "true" ]]; then
    pytest
fi

if [[ "$DEV_SERVER" = "true" ]]; then
    ./manage.py runserver $DEV_SERVER_ADDRESS
else
    uwsgi --ini .prod/uwsgi.ini
fi
