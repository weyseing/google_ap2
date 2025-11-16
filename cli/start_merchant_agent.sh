# !/bin/bash

# log file
rm -rf /app/.logs
mkdir /app/.logs
touch /app/.logs/watch.log

uv run --no-sync --env-file .env python -m roles.merchant_agent