import discord

from discord.ext import commands

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='warn', help='Warn a user for misbehavior')
    async def warn_user(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            await ctx.send('Please provide a reason for the warning.')
        else:
            # Perform the warning action here
            await ctx.send(f'{member.mention} has been warned for: {reason}')

def setup(bot):
    bot.add_cog(Warn(bot))