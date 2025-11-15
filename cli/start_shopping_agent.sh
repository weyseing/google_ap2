# !/bin/bash
uv run --no-sync --env-file .env adk web --host 0.0.0.0 --port 7000 "/app/src/roles" --reload_agents