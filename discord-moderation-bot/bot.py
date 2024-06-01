import discord
from discord.ext import commands
from src.commands import kick, ban, mute, warn
from src.filters import spam_filter, language_filter
from src.settings import config
from logs.moderation_logs import log_moderation_action
from user_management import role_assignment, nickname_changes, user_info
from scheduled_tasks import cleanup_inactive_users

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    await spam_filter.check_spam(message)
    await language_filter.check_language(message)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await kick.kick_member(ctx, member, reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ban.ban_member(ctx, member, reason)

@bot.command()
async def mute(ctx, member: discord.Member, duration=None):
    await mute.mute_member(ctx, member, duration)

@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await warn.warn_member(ctx, member, reason)

@bot.command()
async def set_filter_sensitivity(ctx, sensitivity_level):
    config.set_filter_sensitivity(ctx.guild.id, sensitivity_level)

@bot.command()
async def set_ban_reason(ctx, reason):
    config.set_ban_reason(ctx.guild.id, reason)

@bot.command()
async def set_kick_reason(ctx, reason):
    config.set_kick_reason(ctx.guild.id, reason)

@bot.event
async def on_member_join(member):
    await role_assignment.assign_default_role(member)

@bot.command()
async def change_nickname(ctx, member: discord.Member, new_nickname):
    await nickname_changes.change_nickname(ctx, member, new_nickname)

@bot.command()
async def get_user_info(ctx, member: discord.Member):
    await user_info.get_user_info(ctx, member)

@bot.command()
async def schedule_cleanup(ctx):
    await cleanup_inactive_users.schedule_cleanup(ctx)

bot.run('YOUR_BOT_TOKEN')