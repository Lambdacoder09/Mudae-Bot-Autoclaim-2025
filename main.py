import discord
import asyncio
import itertools

class MyClient(discord.Client):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.content == 'Wished by <@894576628255055892>':
            
            if message.components and message.components[0].children:
                try:
                    await message.channel.send('$rt')
                    await asyncio.sleep(1)

                    await message.components[0].children[0].click()
                    print(f'{self.user} clicked the button.')
                    await asyncio.sleep(20)
                    await message.channel.send('$forcedivorce rem')
                    await asyncio.sleep(3)
                    await message.channel.send('y')

                except Exception as e:
                    print(f"Error clicking button: {e}")
            else:
                print("No components or children found in the message.")
            await self.close()  # Stop the bot after reacting

    async def run_bot(self):
        await self.start(self.token)

async def run_bots_sequentially(tokens):
    for token in itertools.cycle(tokens):
        client = MyClient(token)
        await client.run_bot()
        await asyncio.sleep(10)   # Short delay before starting the next bot

if __name__ == "__main__":
    tokens = [
       "TOKEN1",
      "TOKEN2"
      #AND SO ON 

    ]
    asyncio.run(run_bots_sequentially(tokens))

