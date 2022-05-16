from .twitch_functions.twitch_thumbnails import save_thumbnail
from .twitch_functions.get_client import get_client
from .tesseract_functions.process_image import process_image

def process(user_logins, dir):
    client = get_client()
    filenames = save_thumbnail(user_logins=user_logins, twitch_client=client, dir=dir)
    for filename in filenames:
        process_image(filename)
