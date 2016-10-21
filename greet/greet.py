import discord
from discord.ext import commands

class Greet:
    """Greets people when they login!"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        server = member.server
        await self.bot.send_message(server, "Welcome to " + server.name + " " + member.mention + "! Thanks for joining and enjoy your stay!")

    async def on_member_remove(self, member):
        server = member.server
        await self.bot.send_message(server, member.mention + " has left the Discord server.")

def setup(bot):
    bot.add_cog(Greet(bot))
