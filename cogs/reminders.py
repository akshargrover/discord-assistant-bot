import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio

class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="remind", description="Set a reminder")
    async def remind(self, interaction: discord.Interaction, message: str, seconds: int):
        await interaction.response.send_message(f"⏳ Reminder set! I will remind you in {seconds} seconds.")
        await asyncio.sleep(seconds)
        await interaction.followup.send(f"⏰ Reminder: {message}")

async def setup(bot):
    await bot.add_cog(Reminders(bot))
