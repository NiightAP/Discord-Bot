# bot.py

import os
import dotenv
import logging
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
import asyncio
from itertools import cycle

#log
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

bot = commands.Bot(command_prefix='?')

status = cycle(['ngyt.tk/discordbot', '?help for help'])

#bot connected
# @bot.event
#    print(f'{bot.user} has connected to Discord!')

#bot status
@tasks.loop(seconds=30)
async def change_status(): 
    await bot.change_presence(activity=discord.Game(next(status)))
@bot.event
async def on_ready():
    change_status.start()


# Discord Bot Commands

#ping
@bot.command()
async def ping(ctx):
    await ctx.channel.trigger_typing()
    await ctx.channel.send(f'Pong! {round(bot.latency * 1000)}ms')

#say
@bot.command(pass_contect = True)
async def say(ctx, *args):
    await ctx.channel.trigger_typing()
    msg = ' '.join(args)
    await ctx.message.delete()
    return await ctx.channel.send(msg)

#dev    
@bot.command()
async def dev(ctx):
    await ctx.channel.trigger_typing()
    await ctx.channel.send("Developed by NiightAP: https://ngyt.tk")

#ban
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.channel.trigger_typing()
    await member.ban(reason = reason)
    await ctx.send(f':boom: Member has been banned.')
    await ctx.message.delete()

#pardon
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

#kick
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.delete()
    await ctx.channel.send("Member has been kicked")

#clear
@bot.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

#changenick
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def changenick(ctx, member: discord.Member, nick):
    await ctx.channel.trigger_typing()
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

#bot errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permissions for that command.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send("Please enter all of the required arguments.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.trigger_typing()
        await ctx.send('This command does not exist for this bot.')
        await ctx.message.delete()
    else:
        raise error

bot.run(TOKEN)
