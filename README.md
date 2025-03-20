# Sequential Discord Self-Bot Using `discord.py-self`

This project demonstrates how to create a sequential self-bot using the [`discord.py-self`](https://github.com/dolfies/discord.py-self) library. The bot operates by activating one account at a time to monitor mentions from a specific user, respond accordingly, and then deactivate before the next account takes over.

**Disclaimer:** Automating user accounts (self-bots) is against [Discord's Terms of Service](https://discord.com/terms). Using self-bots can result in account termination. This project is for educational purposes only. Use at your own risk.

## Features

- Sequential activation of multiple Discord accounts.
- Monitors mentions from a specific user.
- Responds with a predefined message and interacts with message components (e.g., buttons).
- Deactivates after interaction, allowing the next account to take over.

## Prerequisites

- Python 3.7 or higher.
- `discord.py-self` library.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/sequential-discord-selfbot.git
   cd sequential-discord-selfbot
   ```


2. **Install Dependencies:**

   ```bash
   pip install discord.py-self
   ```


## Usage

1. **Configure Tokens and User ID:**

   Replace the placeholders in the `tokens` list with your Discord account tokens. Set the `target_user_id` to the ID of the user whose mentions the bot should monitor.

   ```python
   tokens = [
       'your_first_account_token',
       'your_second_account_token',
       # Add more tokens as needed
   ]
   target_user_id = 123456789012345678  # Replace with the target user's ID
   ```


2. **Run the Bot:**

   ```bash
   python bot.py
   ```


   The bot will sequentially activate each account, monitor for mentions from the specified user, respond, and then deactivate before moving to the next account.

## Code Overview

The core functionality is implemented in the `MyClient` class, which inherits from `discord.Client`. The bot listens for messages, checks if the author matches the target user ID, verifies if the bot is mentioned, and then performs the specified actions.


```python
import discord
import asyncio
import itertools

class MyClient(discord.Client):
    def __init__(self, token, target_user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.target_user_id = target_user_id

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author.id == self.target_user_id and self.user in message.mentions:
            await message.channel.send('$rt')
            await asyncio.sleep(1)
            if message.components and message.components[0].children:
                try:
                    await message.components[0].children[0].click()
                    print(f'{self.user} clicked the button.')
                except Exception as e:
                    print(f"Error clicking button: {e}")
            else:
                print("No components or children found in the message.")
            await self.close()  # Stop the bot after reacting

    async def run_bot(self):
        await self.start(self.token)

async def run_bots_sequentially(tokens, target_user_id):
    for token in itertools.cycle(tokens):
        client = MyClient(token, target_user_id)
        await client.run_bot()
        await asyncio.sleep(10)  # Short delay before starting the next bot

if __name__ == "__main__":
    tokens = [
        'your_first_account_token',
        'your_second_account_token',
        # Add more tokens as needed
    ]
    target_user_id = 123456789012345678  # Replace with the target user's ID
    asyncio.run(run_bots_sequentially(tokens, target_user_id))
```


## Important Notes

- **Self-Bot Usage:** Operating self-bots is against Discord's Terms of Service. Use this script responsibly and at your own risk.

- **Account Security:** Keep your account tokens confidential. Exposure can lead to unauthorized access.

- **Rate Limits:** Be mindful of Discord's rate limits to avoid potential restrictions or bans.

## Resources

- [`discord.py-self` Documentation](https://discordpy-self.readthedocs.io/en/latest/)
- [Discord Terms of Service](https://discord.com/terms)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This project is intended for educational purposes only. The use of self-bots is against Discord's Terms of Service and can result in account termination. The author is not responsible for any misuse of this script. 
