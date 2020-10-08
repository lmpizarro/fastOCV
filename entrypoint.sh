#!/bin/env sh

# exec celery -A tasks worker -l INFO &

exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app




