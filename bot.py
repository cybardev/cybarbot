#!/usr/bin/env python3
import os
import subprocess

import discord

from utils import generate_resume

bot = discord.Bot()


@bot.slash_command(
    description="Send a message to the chat",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("msg", description="What to say")
async def say(ctx, msg: str):
    if ctx.guild is None:
        await ctx.respond(msg)
    else:
        await ctx.defer(ephemeral=True)
        await ctx.delete()
        await ctx.channel.send(msg)


@bot.slash_command(
    description="Generate PDF resume from user information in YAML format",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("file", description="YAML input file")
@discord.option("filename", description="PDF file name (without extension)")
async def resumake(ctx, file: discord.Attachment, filename: str = "resume"):
    await ctx.defer()
    await file.save(f"{filename}.yaml")
    await generate_resume(filename)
    await ctx.respond(file=discord.File(f"{filename}.pdf"))


@bot.slash_command(
    description="Get the first video URL from a YouTube search",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("query", description="What to search")
@discord.option("embed", description="Whether to show video embed")
async def yt(ctx, query: str, embed: bool = True):
    cmd = subprocess.run(["ytgo", "-d", query], stdout=subprocess.PIPE, text=True)
    await ctx.respond(cmd.stdout if embed else f"<{cmd.stdout.strip()}>")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
