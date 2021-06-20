from aiohttp import web
from aiohttp.web import Request, Response

from .logs import logger


async def gsi_root(request: Request):
    content = await request.json()
    logger.debug(content)
    return Response(status=200)

app = web.Application()
app.add_routes([web.post('/', gsi_root)])


def run():
    web.run_app(app)
