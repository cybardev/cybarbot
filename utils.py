import asyncio
import contextlib
import logging
import os

import aiohttp
from aiohttp import web

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def _web_handler(request):
    """
    We use this because Render requires free web services to
    bind to a port regardless if it's used in the application
    """
    return web.Response(
        text="Bot has been awakened from sleep. You can use it again now."
    )


async def _bot_server(bot):
    async with bot:
        await bot.start(os.getenv("BOT_TOKEN"))


async def _run_bot(_app, bot):
    task = asyncio.create_task(_bot_server(bot))

    yield

    task.cancel()
    with contextlib.suppress(asyncio.CancelledError):
        await task  # Ensure any exceptions etc. are raised.


def main(bot):
    app = web.Application()
    app.add_routes([web.get("/", _web_handler)])
    app.cleanup_ctx.append(lambda _app: _run_bot(_app, bot))
    web.run_app(app, port=10000)


async def generate_resume(filename):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://resumake.cybar.dev/resume/",
            data={"resume": open(f"{filename}.yaml", "rb")},
        ) as res:
            if res.status == 200:
                pdf_content = await res.read()  # Read response content as bytes
                with open(f"{filename}.pdf", "wb") as pdf_file:
                    pdf_file.write(pdf_content)
            else:
                logger.error(f"Failed to generate resume. Error {res.status}")
