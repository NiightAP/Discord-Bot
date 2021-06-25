import discord
import os
from discord import client
import dotenv
import logging
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    @commands.command()
    async def dev(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.channel.send("Developed by NiightAP: https://ngyt.tk")

def setup(client):
    client.add_cog(Info(client))



