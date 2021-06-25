import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands

    # Kick
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send("Member has been kicked")

    # Ban
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await ctx.channel.trigger_typing()
        await member.ban(reason = reason)
        await ctx.send(f':boom: Member has been banned.')
        await ctx.message.delete()

    # Pardon
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def pardon(self, ctx, *, member):
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

    # Clear
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    # Changenick
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator = True)
    async def changenick(self, ctx, member: discord.Member, nick):
        await ctx.channel.trigger_typing()
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')

    # Lockdown
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send( ctx.channel.mention + " ***Channel is now in lockdown.***")

    # Unlock
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send( ctx.channel.mention + " ***Channel has been unlocked.***")

def setup(client):
    client.add_cog(Moderation(client))
