from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
from pathlib import Path


def get_stream(user_login, twitch_client):
    return twitch_client.get_streams(user_logins=[user_login])[0]


def save_thumbnail(user_login, twitch_client, directory, width=1600, height=900):
    Path(directory).mkdir(parents=True, exist_ok=True)
    stream = get_stream(user_login, twitch_client)
    filename = None
    if stream:
        response = requests.get(stream["thumbnail_url"].format(width=width, height=height))
        img = Image.open(BytesIO(response.content))
        filename=f"{directory}/{stream['user_login']}_{str(datetime.now().timestamp()).split('.')[0]}.png"
        img.save(filename)

    return filename
