# /app/src/roles/merchant_agent/__main__.py

"""Main for the merchant agent."""

from collections.abc import Sequence
from absl import app
import logging

from roles.merchant_agent.agent_executor import MerchantAgentExecutor
from common import server
from inc import func_utilities

AGENT_MERCHANT_PORT = 7001

def main(argv: Sequence[str]) -> None:
  # re-init logger
  func_utilities.setup_colored_logging(level=logging.INFO)

  # agent card
  agent_card = server.load_local_agent_card(__file__)
  
  # run server
  server.run_agent_blocking(
      port=AGENT_MERCHANT_PORT,
      agent_card=agent_card,
      executor=MerchantAgentExecutor(agent_card.capabilities.extensions),
      rpc_url="/a2a/merchant_agent",
  )

if __name__ == "__main__":
  app.run(main)
