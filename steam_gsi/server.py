import asyncio
import signal
from aiohttp import web
from aiohttp.web import Request, Response

from .logs import logger


class Server:
    def __init__(self, host: str = 'localhost', port: int = 3000):
        self.__host = host
        self.__port = port
        self.__app = web.Application()

        self.__app.add_routes([web.post('/', self.gsi_handler)])

    async def gsi_handler(self, request: Request):
        content = await request.json()
        logger.debug(f"Incoming event: {content}")
        return Response(status=200)

    async def run(self):
        # Raise KeyboardInterrupt on SIGTERM
        def handle_sigterm(sig, frame):
            raise KeyboardInterrupt

        signal.signal(signal.SIGTERM, handle_sigterm)

        runner = web.AppRunner(self.__app)
        await runner.setup()
        site = web.TCPSite(runner, self.__host, self.__port)
        await site.start()

        # Block until KeyboardInterrupt is detected
        try:
            while True:
                await asyncio.sleep(3600)
        except KeyboardInterrupt:
            await runner.cleanup()
