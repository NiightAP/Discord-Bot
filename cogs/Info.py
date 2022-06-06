import discord
from discord.ext import commands

client = discord.Client()

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands

    # Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    
    # Dev
    @commands.command()
    async def dev(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.send("**@NiightGamez#1009**" + " Developed by NiightAP: https://github.com/niightap")

    # Source
    @commands.command()
    async def source(self, ctx):
        await ctx.send(f"**{ctx.bot.user}** is powered by this source code:\nhttps://github.com/NiightAP/Discord-Bot")

    # Servers
    @commands.command(pass_context=True)
    async def servers(self, ctx):
        await ctx.channel.send("I'm in " + str(len(client.guilds)) + " servers!")

    # Invite
    @commands.command()
    async def invite(self, ctx):
        invitelink = "Invite NiightAP to your server with this link: \nhttps://niightap.fanlink.to/botinv"
        await ctx.message.delete()
        await ctx.author.send(invitelink)

def setup(client):
    client.add_cog(Info(client))



