import discord

from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                await ctx.send("You cannot kick an administrator.")
            else:
                await member.kick(reason=reason)
                await ctx.send(f'{member.mention} has been kicked.')
        else:
            await ctx.send("You do not have permission to kick members.")

def setup(bot):
    bot.add_cog(Kick(bot))