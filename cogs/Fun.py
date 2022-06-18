from gettext import install
import discord
import random
from typing import Optional
from random import choice
from discord import Member
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands

    # Hello
    @commands.command()
    async def say_hello(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")

    # Say
    @commands.command(pass_contect = True)
    async def say(self, ctx, *args):
        await ctx.channel.trigger_typing()
        msg = ' '.join(args)
        await ctx.message.delete()
        return await ctx.channel.send(msg)

    # Slap
    @commands.command()
    async def slap(self, ctx, member: Member, *, reason: Optional[str] = "for no reason"):
        await ctx.channel.trigger_typing()
        await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reason}!")

    # Coinflip
    @commands.command()
    async def coinflip(self, ctx):
        coinsides = ["Heads", "Tails"]
        await ctx.channel.trigger_typing()
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    # Slots
    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slots(self, ctx):
        await ctx.channel.trigger_typing()
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

def setup(client):
    client.add_cog(Fun(client))

