#!/bin/bash

# Start the worker
echo "Starting the worker"
celery -A api worker -l info
