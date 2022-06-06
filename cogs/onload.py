import discord
from discord.ext import commands

client = discord.Client()

class Onload(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        print(str(len(client.guilds)) +  ' servers!')

def setup(client):
    client.add_cog(Onload(client))