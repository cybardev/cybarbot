#!/usr/bin/env python3

import os

import discord

bot = discord.Bot()

# ----------------- TODO: MAKE CHANGES BELOW ----------------- #


@bot.slash_command(
    description="Say hello",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("name", description="Who to greet")
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello, {name}!")


# ----------------- TODO: MAKE CHANGES ABOVE ----------------- #


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
