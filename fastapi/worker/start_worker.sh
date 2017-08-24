#!/usr/bin/env bash

celery -A fastapi.fastapi.celery -l info worker