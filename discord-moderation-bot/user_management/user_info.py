import discord

class UserInfo:
    def __init__(self, client):
        self.client = client

    async def get_user_info(self, ctx, user_id):
        user = await self.client.fetch_user(user_id)
        if user:
            user_info_embed = discord.Embed(title="User Information", color=discord.Color.blue())
            user_info_embed.add_field(name="Username", value=user.name, inline=False)
            user_info_embed.add_field(name="User ID", value=user.id, inline=False)
            user_info_embed.add_field(name="Avatar URL", value=user.avatar_url, inline=False)
            await ctx.send(embed=user_info_embed)
        else:
            await ctx.send("User not found.")

    async def change_nickname(self, ctx, nickname):
        try:
            await ctx.author.edit(nick=nickname)
            await ctx.send(f"Nickname changed to {nickname}.")
        except discord.Forbidden:
            await ctx.send("I don't have permission to change nicknames.")

    async def assign_role(self, ctx, role_name):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            try:
                await ctx.author.add_roles(role)
                await ctx.send(f"Role {role_name} assigned successfully.")
            except discord.Forbidden:
                await ctx.send("I don't have permission to assign roles.")
        else:
            await ctx.send("Role not found.")

    async def run_command(self, ctx, command, *args):
        if command == "info":
            await self.get_user_info(ctx, *args)
        elif command == "nickname":
            await self.change_nickname(ctx, *args)
        elif command == "role":
            await self.assign_role(ctx, *args)