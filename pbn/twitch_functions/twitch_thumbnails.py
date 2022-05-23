from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
from pathlib import Path


def get_streams(user_logins, twitch_client):
    return twitch_client.get_streams(user_logins=user_logins)[:len(user_logins)]

def save_thumbnail(user_logins, twitch_client, dir, width=1600, height=900):
    Path(dir).mkdir(parents=True, exist_ok=True)
    streams = get_streams(user_logins, twitch_client)
    filenames = []
    for stream in streams:
        response = requests.get(stream["thumbnail_url"].format(width=width, height=height))
        img = Image.open(BytesIO(response.content))
        filename=f"{dir}/{stream['user_login']}_{str(datetime.now().timestamp()).split('.')[0]}.png"
        img.save(filename)
        filenames.append(filename)

    return filenames
