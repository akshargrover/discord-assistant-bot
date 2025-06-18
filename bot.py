import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = False  # Optional

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands.")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await member.send(f"👋 Welcome to {member.guild.name}, {member.name}!")

async def main():
    async with bot:
        # Await loading all cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.start(os.getenv("DISCORD_TOKEN"))

# Run the async main
asyncio.run(main())