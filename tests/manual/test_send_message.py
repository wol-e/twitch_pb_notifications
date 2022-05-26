from pbn.telegram_bot.wolle_bot_bot_send_message import send_message
import os

message = "my test message"
token = os.getenv('wolle_bot_bot_token')
pbn_chat_id = os.getenv('pbn_chat_id')

if __name__ == "__main__":
    send_message(chat_id=pbn_chat_id, token=token, message=message)
