import os

# Discord bot configuration settings
class Config:
    # Bot token for authentication
    BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

    # Prefix for bot commands
    COMMAND_PREFIX = '!'

    # Moderation settings
    MODERATION_SETTINGS = {
        'filter_sensitivity': 'medium',
        'ban_reason': 'Violating server rules',
        'kick_reason': 'Disruptive behavior',
        'warn_reason': 'Breaking server guidelines'
    }

    # Logging settings
    LOGGING_SETTINGS = {
        'log_file': 'logs/moderation_logs.txt',
        'log_format': '%(asctime)s - %(levelname)s - %(message)s'
    }

    # User management settings
    USER_MANAGEMENT_SETTINGS = {
        'role_assignment_roles': ['admin', 'moderator', 'member'],
        'nickname_change_format': 'User-{}',
        'user_info_fields': ['username', 'discriminator', 'join_date']
    }

    # Scheduled tasks settings
    SCHEDULED_TASKS_SETTINGS = {
        'cleanup_interval': 'daily',
        'cleanup_threshold': 30
    }

    # Interface settings
    INTERFACE_SETTINGS = {
        'interface_file': 'interface/index.html',
        'style_file': 'interface/style.css'
    }