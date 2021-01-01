# bot.py

import os
import dotenv

import discord
from dotenv import load_dotenv
from discord.ext import commands

prefix = "?"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('ngyt.tk/discordbot'))

#@client.event
#async def ping(ctx):

    # Get the latency of the bot
#    latency = client.latency
#    await ctx.send(latency)


client.run(TOKEN)