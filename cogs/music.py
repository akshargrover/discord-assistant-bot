import discord
from discord import app_commands
from discord.ext import commands
import youtube_dl
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="play", description="Play music from YouTube")
    async def play(self, interaction: discord.Interaction, url: str):
        if not interaction.user.voice:
            await interaction.response.send_message("🚫 Join a voice channel first.")
            return

        vc = await interaction.user.voice.channel.connect()
        await interaction.response.send_message("🎶 Playing audio...")

        ydl_opts = {'format': 'bestaudio'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['url']

        vc.play(discord.FFmpegPCMAudio(URL), after=lambda e: print('Done', e))

async def setup(bot):
    await bot.add_cog(Music(bot))