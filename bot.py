# bot.py

import os
import dotenv
import logging
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
import asyncio
from itertools import cycle

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

bot = commands.Bot(command_prefix='?')

status = cycle(['ngyt.tk/discordbot', '?help for help'])

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# Discord Bot Commands

@bot.command()
async def ping(ctx):
    await ctx.channel.trigger_typing()
    await ctx.channel.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def print(ctx, arg):
	await ctx.channel.send(arg) 

@bot.command(pass_contect = True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def say(ctx, *args):
    await ctx.channel.trigger_typing()
    msg = ' '.join(args)
    await ctx.message.delete()
    return await ctx.channel.send(msg)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('This command is on cooldown, you may use it again in a little bit.')
    
@bot.command()
async def dev(ctx):
    await ctx.channel.trigger_typing()
    await ctx.channel.send("Developed by NiightAP: https://ngyt.tk")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.channel.trigger_typing()
    await member.ban(reason = reason)
    await ctx.send(f':boom: Member has been banned.')
    await ctx.message.delete()
@bot.command()
@commands.has_permissions(administrator = True)
async def pardon(ctx, *, member):
    await ctx.channel.trigger_typing()
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.channel.trigger_typing()
            await ctx.guild.unban(user)
            await ctx.send(f'Unabnned {user.mention}')
            return

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.channel.trigger_typing()
    await member.kick(reason=reason)
    await ctx.message.delete()
    await ctx.channel.send("Member has been kicked")



bot.run(TOKEN)
