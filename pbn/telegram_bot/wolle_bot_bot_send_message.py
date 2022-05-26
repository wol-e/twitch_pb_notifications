import asyncio
import os

from telegram import Bot

from dotenv import load_dotenv
load_dotenv()


async def async_send_message(chat_id, token, message):
    bot = Bot(token=token)
    async with bot:
        await bot.send_message(
            chat_id=chat_id,
            text=message
        )

def send_message(chat_id, token, message):
    asyncio.run(async_send_message(chat_id, token, message))

#if __name__ == '__main__':
#    asyncio.run(async_send_message())
