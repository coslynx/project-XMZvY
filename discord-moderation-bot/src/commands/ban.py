import discord

from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', help='Ban a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot ban yourself.")
            return

        if member == self.bot.user:
            await ctx.send("You cannot ban the bot.")
            return

        if member.top_role >= ctx.author.top_role:
            await ctx.send("You do not have permission to ban this user.")
            return

        if reason:
            await member.ban(reason=reason)
            await ctx.send(f'{member} has been banned for {reason}.')
        else:
            await member.ban()
            await ctx.send(f'{member} has been banned.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to ban members.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify the user to ban.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        else:
            await ctx.send("An error occurred while processing the command.")

def setup(bot):
    bot.add_cog(Ban(bot))