import os

from pbn.twitch_api.get_client import get_client
from pbn.twitch_api.streams import save_thumbnail

if __name__ == "__main__":
    client = get_client()

    files = save_thumbnail(
        user_logins=[
            "ArmadaUGS",
            "larxa",
        ],
        twitch_client=client,
        directory=os.getcwd() + "/data"
    )

    print(files)