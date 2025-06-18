import discord
from discord import app_commands
from discord.ext import commands
import requests
import os

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv("WEATHER_API_KEY")

    @app_commands.command(name="weather", description="Get current weather info for a city")
    async def weather(self, interaction: discord.Interaction, city: str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        res = requests.get(url).json()
        if res.get("cod") != 200:
            await interaction.response.send_message("❌ City not found.")
        else:
            desc = res['weather'][0]['description'].capitalize()
            temp = res['main']['temp']
            await interaction.response.send_message(f"🌤 Weather in {city.title()}: {desc}, {temp}°C")

async def setup(bot):
    await bot.add_cog(Weather(bot))