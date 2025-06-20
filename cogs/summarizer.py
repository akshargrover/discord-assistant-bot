import discord
from discord import app_commands
from discord.ext import commands
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class Summarizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

    @app_commands.command(name="summarize", description="Summarize given text")
    async def summarize(self, interaction: discord.Interaction, text: str):
        await interaction.response.defer()
        prompt = f"Summarize this:{text}"
        result = self.llm.invoke(prompt)
        await interaction.followup.send(result[:2000])

async def setup(bot):
    await bot.add_cog(Summarizer(bot))