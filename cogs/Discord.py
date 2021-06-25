import discord
from discord.ext import commands



class Discord_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Avatar
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        await ctx.send(f"Avatar to **{user.name}** \n{user.avatar_url_as(size=1024)}")

def setup(bot):
    bot.add_cog(Discord_Info(bot))