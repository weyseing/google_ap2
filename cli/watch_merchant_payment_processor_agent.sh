# !/bin/bash

find /app/src/roles/merchant_payment_processor_agent/ -name "*.py" | entr -r /app/cli/start_merchant_payment_processor_agent.sh