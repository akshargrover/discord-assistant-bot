import discord
from discord import app_commands
from discord.ext import commands
from rag.qa_chain import get_qa_chain

class AIAssistant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.qa_chain = get_qa_chain()

    @app_commands.command(name="ask", description="Ask a question to the AI assistant")
    async def ask(self, interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        try:
            response = self.qa_chain.invoke({"question": question})
            # Extract the answer from the dictionary
            answer = response.get('result') or response.get('answer') or str(response)
            if not answer:
                answer = "Sorry, I couldn't find an answer."
            await interaction.followup.send(answer[:2000])  # Discord message limit
        except Exception as e:
            print(f"Error in /ask: {e}")
            await interaction.followup.send("An error occurred while processing your question.")

async def setup(bot):
    await bot.add_cog(AIAssistant(bot))
