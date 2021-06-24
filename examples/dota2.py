import asyncio
import logging

from steam_gsi.gsiserver import GSIServer, logger

logger.setLevel(logging.DEBUG)
server = GSIServer(tokens=['hello1234'])

loop = asyncio.get_event_loop()

loop.run_until_complete(server.run())
