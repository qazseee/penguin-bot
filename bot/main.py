import os

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)


async def main():

    # load extensions
    await bot.load_extension("help_cog")
    await bot.load_extension("music_cog_v2")
    await bot.load_extension("dictionary_cog")
    await bot.load_extension("translate_cog")

    # start the bot with our token
    await bot.start(os.getenv("BOT_TOKEN"))

    # TODO: Play a song from spotify link


if __name__ == "__main__":
    asyncio.run(main())

# Current version is not good. Playlist queue keeps messing up. Working on it.
# Added music cog v2, haven't tested yet
