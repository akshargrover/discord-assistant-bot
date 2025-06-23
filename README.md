# Discord Assistant Bot

A modular, extensible Discord bot with multiple assistant features, built using [discord.py](https://discordpy.readthedocs.io/). The bot supports commands for AI assistance, music, moderation, reminders, news, weather, and more, organized as separate cogs for easy management and scalability.

## Features
- **AI Assistant**: Chat with an AI assistant directly in Discord.
- **Music**: Play, pause, and manage music in voice channels.
- **Moderation**: Tools for server moderation (kick, ban, etc.).
- **Reminders**: Set and manage reminders.
- **News**: Fetch the latest news headlines.
- **Weather**: Get current weather updates.
- **Summarizer**: Summarize long texts or articles.
- **RAG (Retrieval-Augmented Generation)**: Integrate with FAISS for document search and Q&A.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd discord-assistant-bot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Discord bot token:
     ```env
     DISCORD_TOKEN=your-bot-token-here
     ```

## Running the Bot

```bash
python bot.py
```

The bot will automatically load all cogs from the `cogs/` directory.

## Directory Structure

```
discord-assistant-bot/
├── bot.py                # Main entry point
├── cogs/                 # Bot features (AI, music, moderation, etc.)
├── rag/                  # Retrieval-Augmented Generation modules
├── data/                 # Data files and FAISS indexes
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

## Adding or Editing Cogs
- Add new features by creating a new `.py` file in the `cogs/` directory.
- Each cog should define a class that inherits from `commands.Cog`.
- The bot will auto-load all cogs on startup.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
