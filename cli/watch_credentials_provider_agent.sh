# !/bin/bash

find /app/src/roles/credentials_provider_agent/ -name "*.py" | entr -r /app/cli/start_credentials_provider_agent.sh