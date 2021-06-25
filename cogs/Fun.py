import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(pass_context = True)
    async def say(self, ctx, *args):
        await ctx.channel.trigger_typing()
        msg = ' '.join(args)
        await ctx.message.delete()
        return await ctx.channel.send(msg)

def setup(client):
    client.add_cog(Fun(client))

