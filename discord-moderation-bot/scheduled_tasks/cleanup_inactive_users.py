import discord
from discord.ext import tasks
from datetime import datetime, timedelta

class CleanupInactiveUsersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cleanup_inactive_users.start()

    def cog_unload(self):
        self.cleanup_inactive_users.cancel()

    @tasks.loop(hours=24)
    async def cleanup_inactive_users(self):
        inactive_time = datetime.now() - timedelta(days=30)
        guild = self.bot.get_guild(GUILD_ID)  # Replace GUILD_ID with actual guild ID

        for member in guild.members:
            if member.joined_at < inactive_time:
                await member.kick(reason="Inactive for 30 days")

def setup(bot):
    bot.add_cog(CleanupInactiveUsersCog(bot))