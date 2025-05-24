import discord
from bot.config import create_discord_config
from core.assistant import ask_stilgar

discord_config = create_discord_config()


class StilgarClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if not message.content.strip():
            return

        if message.channel.name == "stilgar-room":
            response = ask_stilgar(message.content)
            await message.channel.send(response)


client = StilgarClient(intents=discord_config["intents"])


@client.event
async def on_ready():
    print(f"Stilgar está pronto como {client.user}")


client.run(discord_config["token"])
