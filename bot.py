import discord
import os
import dotenv
import logging
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

client = discord.Client()
client =  commands.Bot(command_prefix = '?')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

status = cycle(['https://github.com/niightap', '?help for help'])

#bot status
@tasks.loop(seconds=30)
async def change_status(): 
    await client.change_presence(activity=discord.Game(next(status)))
@client.event
async def on_ready():
    change_status.start()

#cogs
@client.command(pass_context = True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(pass_context = True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
