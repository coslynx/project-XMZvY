import discord

class RoleAssignment:
    def __init__(self, client):
        self.client = client

    async def assign_role(self, member, role_name):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
            return f"Role {role_name} successfully assigned to {member.display_name}."
        else:
            return f"Role {role_name} not found in the server."

    async def remove_role(self, member, role_name):
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.remove_roles(role)
            return f"Role {role_name} successfully removed from {member.display_name}."
        else:
            return f"Role {role_name} not found in the server."

    async def change_nickname(self, member, new_nickname):
        try:
            await member.edit(nick=new_nickname)
            return f"Nickname changed to {new_nickname} for {member.display_name}."
        except discord.Forbidden:
            return "Bot does not have permission to change nickname."

    async def get_user_info(self, member):
        user_info = f"User Information for {member.display_name}:\n"
        user_info += f"User ID: {member.id}\n"
        user_info += f"Joined at: {member.joined_at}\n"
        user_info += f"Roles: {', '.join([role.name for role in member.roles])}\n"
        return user_info

# Instantiate RoleAssignment class with the Discord client
role_assignment = RoleAssignment(client)