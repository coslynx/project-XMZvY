import discord

class NicknameChanges:
    def __init__(self, client):
        self.client = client

    async def change_nickname(self, member, new_nickname):
        try:
            await member.edit(nick=new_nickname)
        except discord.Forbidden:
            print("Bot does not have permission to change nickname.")
        except discord.HTTPException:
            print("Failed to change nickname due to an HTTP error.")
        except discord.InvalidArgument:
            print("Invalid nickname provided.")

    async def on_nickname_change(self, before, after):
        if before.nick != after.nick:
            print(f"Nickname changed from {before.nick} to {after.nick}")

    async def process_nickname_change(self, member, new_nickname):
        await self.change_nickname(member, new_nickname)
        await self.on_nickname_change(member, member)

# Instantiate the class with the Discord client
nickname_changes = NicknameChanges(client)