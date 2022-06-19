import discord
from datetime import datetime, timedelta
from time import time
from turtle import color
from discord import Activity, ActivityType, Embed
from discord import __version__ as discord_version
from discord.ext import commands
from psutil import Process, virtual_memory
from platform import python_version


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

    # Stats // Currently broken
    @commands.command()
    async def stats(self, ctx):
        embed = Embed(title="Bot Stats",
                    color=ctx.author.color,
                    thumbnail=self.client.user.avatar_url,
                    timestamp=datetime.utcnow()) 
        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time()) 
        fields = [
            ("Python Version", python_version(), True),
            ("Discord Version", discord_version, True),
            ("Uptime", uptime, True),
            ("Users", f"{self.client.guild.member_count:,}", True)
        ] 
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline) 
        await ctx.send(embed=embed)

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



