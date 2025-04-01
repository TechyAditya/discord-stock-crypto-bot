# main.py
# Entry point for the Discord bot.

import discord
from discord.ext import commands
from bot.config import BOT_TEST_CHANNEL_ID, CRYPTO_CHANNEL_ID, DISCORD_TOKEN, COMMAND_PREFIX, ALLOWED_CHANNELS, STOCKS_CHANNEL_ID
from bot.handlers.query_handler import handle_help, handle_query
from bot.handlers.stocks_handler import handle_stocks
from bot.handlers.crypto_handler import handle_crypto
from bot.utils.helper_functions import log_command

# Create a bot instance with the designated command prefix.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(aliais=["ping", "hi", "hello"])
async def test(ctx):
    if str(ctx.channel.id) not in [STOCKS_CHANNEL_ID, CRYPTO_CHANNEL_ID, BOT_TEST_CHANNEL_ID]:
        return
    log_command(ctx.author.name, "test")
    await ctx.send("Bot is alive!")


@bot.command(aliases=["h"])
async def help(ctx, *args):
    if str(ctx.channel.id) not in ALLOWED_CHANNELS:
        return
    log_command(ctx.author.name, args)
    await ctx.send(handle_help(args, ctx.channel.id))


@bot.command(aliases=["s"])
async def stocks(ctx, *args):
    if str(ctx.channel.id) not in [STOCKS_CHANNEL_ID, BOT_TEST_CHANNEL_ID]:
        return
    log_command(ctx.author.name, args)
    await ctx.send(handle_stocks(args, ctx.channel.id))


@bot.command(aliases=["c"])
async def crypto(ctx, *args):
    if str(ctx.channel.id) not in [CRYPTO_CHANNEL_ID, BOT_TEST_CHANNEL_ID]:
        return
    log_command(ctx.author.name, args)
    await ctx.send(await handle_crypto(args, ctx.author.mention, ctx.channel.id))


bot.run(DISCORD_TOKEN)
