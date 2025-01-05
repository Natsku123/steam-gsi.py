import asyncio
import signal
from aiohttp import web
from aiohttp.web import Request, Response
from typing import Union, List

from .logs import logger
from .datastorage import update_game_state
from .events import event_trigger

from .games.dota2 import GameState as Dota2GameState

# SLEEP DELAY is the maximum delay that the server takes to stop, currently
# is pretty high since it gives more cpu time for other asynchronous functions.
SLEEP_DELAY = 5


class GSIServer:
    def __init__(
            self, host: str = 'localhost', port: int = 3000,
            tokens: Union[List[str], str] = None
    ):
        """
        Initialize a server

        :param host: interface IP Address (default localhost)
        :param port: server port
        :param tokens: tokens allowed to post data, list of strings and
        a string is accepted
        """
        self.__host = host
        self.__port = port
        self.__app = web.Application()

        self.__running = False

        #
        if isinstance(tokens, list):
            self.__tokens = tokens
        elif isinstance(tokens, str):
            self.__tokens = [tokens]
        else:
            self.__tokens = []

        self.__app.add_routes([web.post('/', self.gsi_handler)])

    def check_token(self, token: str) -> bool:
        """
        Check if token is valid

        :param token: string
        :return: bool of validity
        """
        return token in self.__tokens

    async def gsi_handler(self, request: Request) -> Response:
        """
        GSI Handler, default root post handler

        :returns 401 if token is not present or valid
        :returns 200 if successful

        :param request: Incoming request
        :return: Response
        """
        content = await request.json()
        logger.debug(f"Incoming event: {content}")

        # Check that token is sent and is valid
        if 'auth' not in content or 'token' not in content['auth'] or \
                not self.check_token(content['auth']['token']):
            return Response(status=401)

        # Game State Provider check
        if 'provider' in content:

            # If Provider is Dota 2, update Dota 2 Game State
            if content['provider']['name'] == "Dota 2":

                # Updated game state with actual object
                gs = update_game_state(
                    content, content['auth']['token'], Dota2GameState
                )

                # Trigger events registered events
                event_trigger(gs)
            else:
                logger.error(
                    f"ImplementationError: Game state updates for "
                    f"{content['provider']['name']} do not exist."
                )

        return Response(status=200)

    def handle_stops(self, sig, frame):
        """
        Handle stop signals

        :param sig: not used
        :param frame: not used
        :return:
        """
        self.__running = False
        logger.info("Stopping...")

    async def run(self):
        """
        Run server until stopped.

        :return:
        """
        logger.info("Setting up GSI Server...")
        self.__running = True

        # Register signal catches for stopping
        signal.signal(signal.SIGTERM, self.handle_stops)
        signal.signal(signal.SIGINT, self.handle_stops)

        # Setup server
        runner = web.AppRunner(self.__app)
        await runner.setup()
        site = web.TCPSite(runner, self.__host, self.__port)

        logger.info("Starting GSI Server...")
        await site.start()

        # Block until stopped
        while self.__running:
            await asyncio.sleep(SLEEP_DELAY)

        await runner.cleanup()

