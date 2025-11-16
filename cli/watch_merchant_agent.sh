# !/bin/bash

find /app/src/roles/merchant_agent/ -name "*.py" | entr -r /app/cli/start_merchant_agent.sh