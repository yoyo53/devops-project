import discord
import sys
import os
import dotenv

dotenv.load_dotenv()

CHANNEL = int(os.getenv('DISCORD_CHANNEL'))
TOKEN = os.getenv('DISCORD_TOKEN')


class LogBot(discord.Client):
    def __init__(self, channel, message):
        super().__init__(intents=discord.Intents.all())
        self.channel = channel
        self.message = message

    async def on_ready(self):
        await self.get_channel(self.channel).send(self.message)
        await self.close()


if __name__ == '__main__':
    args = sys.argv[1:]

    bot = LogBot(CHANNEL, ' '.join(args))
    bot.run(TOKEN)