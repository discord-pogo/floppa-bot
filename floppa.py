import os
import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

token = os.getenv("FLOPPA_TOKEN")

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
guild_ids = [733665939198967852]
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
@slash.slash(name="link", description="Add MC name to database", options=[create_option(name="account", description="Minecraft account name", option_type=3, required=True)],  guild_ids=guild_ids)
async def _link(ctx, account: str):
    if " " in account:
        await ctx.send("Account failed to link, contains space")
    else: await ctx.send("✅ Account linked: " + account)

client.run(token)