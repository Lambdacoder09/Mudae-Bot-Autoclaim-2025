import discord
from discord.ext import tasks
import asyncio
import itertools
import json
class MyClient(discord.Client):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        # Add your bot's functionality here
        await self.close()

    async def run_bot(self):
        await self.start(self.token)

async def run_bots_sequentially(tokens):
    for token in (tokens):
        client = MyClient(token)
        await client.run_bot()
        await asyncio.sleep(1)  # Short delay before starting the next bot
if __name__ == "__main__":
    # Load tokens from JSON file
    with open("tokens.json", "r") as file:
        data = json.load(file)
        tokens = data["tokens"]
        asyncio.run(run_bots_sequentially(tokens))
