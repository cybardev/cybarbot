import asyncio
import contextlib
import logging
import os
from datetime import datetime, timezone, timedelta

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
    web.run_app(app, port=int(os.getenv("BOT_PORT", 10000)))


def get_timestamp(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    second: int,
    tz_offset: str,
    fmt: str,
):
    tz_h = int(tz_offset.split(":")[0])
    tz_m = int(tz_offset.split(":")[1]) if ":" in tz_offset else 0
    d = datetime(
        year,
        month,
        day,
        hour,
        minute,
        second,
        tzinfo=timezone(
            timedelta(
                hours=tz_h,
                minutes=tz_m,
            )
        ),
    )
    return f"<t:{int(d.timestamp())}:{fmt}>"
