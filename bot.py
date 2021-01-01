# bot.py

import os
import dotenv

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('github.com/niightap/discord-bot'))


# Discord Bot Commands

@bot.command()
async def ping(ctx):
    await ctx.channel.send("Pong")

@bot.command()
async def print(ctx, arg):
	await ctx.channel.send(arg)    


# help command



bot.run(TOKEN)
