#!/usr/bin/env bash

celery -A fastapi.worker.tasks worker -l info