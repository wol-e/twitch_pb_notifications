from .twitch_functions.twitch_thumbnails import get_streams, save_thumbnail
from .twitch_functions.get_client import get_client
from .tesseract_functions.process_image import process_image

def process(user_logins, dir, preprocess, return_steps=False):
    client = get_client()
    filenames = save_thumbnail(user_logins=user_logins, twitch_client=client, dir=dir)
    returns = [process_image(filename, preprocess=preprocess, return_steps=return_steps) for filename in filenames]
    if return_steps:
        return returns


def check_for_online(user_logins):
    client = get_client()
    streams = get_streams(user_logins=user_logins, twitch_client=client)
    print(streams)
    pass
