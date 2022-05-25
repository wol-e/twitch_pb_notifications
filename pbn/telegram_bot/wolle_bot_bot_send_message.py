import asyncio
import os

from telegram import Bot

from dotenv import load_dotenv
load_dotenv()


async def main():
    wolle_bot_bot = Bot(token=os.getenv('wolle_bot_bot_token'))
    pbn_chat_id = os.getenv('pbn_chat_id')
    async with wolle_bot_bot:
        await wolle_bot_bot.send_message(
            chat_id=pbn_chat_id,
            text="Hi group!"
        )

if __name__ == '__main__':
    
    asyncio.run(main())