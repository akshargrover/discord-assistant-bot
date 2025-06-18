import discord
from discord import app_commands
from discord.ext import commands
import requests
import os

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv("NEWS_API_KEY")

    @app_commands.command(name="news", description="Get latest news headlines")
    async def news(self, interaction: discord.Interaction, topic: str = "technology"):
        url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={self.api_key}&language=en&pageSize=3"
        res = requests.get(url).json()
        articles = res.get("articles", [])
        if not articles:
            await interaction.response.send_message("❌ No news found.")
        else:
            headlines = "\n\n".join([f"📰 {a['title']}\n{a['url']}" for a in articles])
            await interaction.response.send_message(headlines)

async def setup(bot):
    await bot.add_cog(News(bot))