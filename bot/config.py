import os
import discord
from dotenv import load_dotenv

load_dotenv()


def create_discord_config():
    intents = discord.Intents.default()
    intents.message_content = True

    token = os.getenv("DISCORD_BOT_TOKEN")
    return {"intents": intents, "token": token}
