import twitch
import os

from PIL import Image
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

from .twitch_functions.twitch_thumbnails import save_thumbnail
from .tesseract_functions.process_image import process_image

load_dotenv()

client = twitch.TwitchHelix(
    client_id=os.getenv("twitch_api_client_id"),
    client_secret=os.getenv("twitch_api_client_secret"),
    scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS]
)

client.get_oauth()

def process(user_logins, twitch_client, dir):
    save_thumbnail(user_logins=user_logins, twitch_client=client, dir=dir)
    process_image(filename_png)
