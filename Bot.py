import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

#loading in token for colby gaming bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = commands.Bot(command_prefix="/", intents=intents)

client.remove_command('load')
client.remove_command('unload')

'''
Commands are loaded in through extensions called cogs in the dir /cogs
'''

@client.command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print('Colby Gaming Bot is online')



client.run(TOKEN)