import discord
import os
from discord import client
import dotenv
import logging
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(pass_contect = True)
    async def say(self, ctx, *args):
        await ctx.channel.trigger_typing()
        msg = ' '.join(args)
        await ctx.message.delete()
        return await ctx.channel.send(msg)

def setup(client):
    client.add_cog(Fun(client))

