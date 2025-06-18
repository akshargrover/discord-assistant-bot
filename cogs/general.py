import discord
from discord import app_commands
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot responsiveness")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("🏓 Pong! I'm alive.")

async def setup(bot):
    await bot.add_cog(General(bot))