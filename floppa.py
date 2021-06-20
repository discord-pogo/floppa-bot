import os
import discord
from discord_slash import SlashCommand

token = os.getenv("FLOPPA_TOKEN")

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
guild_ids = [733665939198967852]
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
@slash.slash(name="test",  guild_ids=guild_ids)
async def _test(ctx):
    await ctx.send("kys!")

client.run(token)