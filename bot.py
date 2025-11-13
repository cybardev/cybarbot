#!/usr/bin/env python3
import subprocess
from datetime import datetime

import discord

from utils import main, get_timestamp

bot = discord.Bot()


@bot.slash_command(description="Send a message to the chat")
@discord.option("msg", description="What to say")
async def say(ctx, msg: str):
    if ctx.interaction.context == discord.InteractionContextType.guild:
        await ctx.defer(ephemeral=True)
        await ctx.delete()
        await ctx.channel.send(msg)
    else:
        await ctx.respond(msg)


@bot.slash_command(description="Generate Discord timestamp for a given date and time")
@discord.option("year", description="Year for timestamp")
@discord.option("month", description="Month for timestamp")
@discord.option("day", description="Day for timestamp")
@discord.option("hour", description="Hour for timestamp")
@discord.option("minute", description="Minutes for timestamp")
@discord.option("second", description="Seconds for timestamp")
@discord.option("tz", description="Timezone for timestamp (e.g. '-3:30')")
@discord.option("fmt", description="Format for timestamp (e.g. 'R', 't', etc.)")
async def timestamp(
    ctx,
    year: int = datetime.now().year,
    month: int = datetime.now().month,
    day: int = datetime.now().day,
    hour: int = datetime.now().hour,
    minute: int = datetime.now().minute,
    second: int = datetime.now().second,
    tz: str = "0",
    fmt: str = "R",
):
    await ctx.defer()
    ts = get_timestamp(year, month, day, hour, minute, second, tz, fmt)
    await ctx.respond(ts)


@bot.slash_command(description="Get the first video URL from a YouTube search")
@discord.option("query", description="What to search")
@discord.option("embed", description="Whether to show video embed")
async def yt(ctx, query: str, embed: bool = True):
    cmd = subprocess.run(["ytgo", "-d", query], stdout=subprocess.PIPE, text=True)
    await ctx.respond(cmd.stdout if embed else f"<{cmd.stdout.strip()}>")


if __name__ == "__main__":
    main(bot)
