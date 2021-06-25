import discord
import os
from discord.errors import ClientException
import dotenv
import logging
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

client = discord.Client()

class Onload(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

def setup(client):
    client.add_cog(Onload(client))