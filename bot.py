import discord
import os
import dotenv
import logging
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv
from itertools import cycle

from setuptools import Command

client = discord.Client()
client =  commands.Bot(command_prefix = '?')
slash = SlashCommand(client, sync_commands=True)

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

# Errors
async def on_error(self, err, *args, **kwargs):
    if err == "on_command_error":
        await args[0].send("Something went wrong.")

    raise

async def on_command_error(self, ctx, exc):
    if isinstance(exc, CommandNotFound):
        pass
    
    elif hasattr(exc, ["originaal"]):
        raise exc.original
    
    else: 
        raise exc

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
