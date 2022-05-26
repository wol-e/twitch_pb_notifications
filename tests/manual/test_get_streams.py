from pbn.twitch_api.streams import get_streams
from pbn.twitch_api.get_client import get_client

if __name__ == "__main__":
    client = get_client()
    streams = get_streams(user_logins=["armadaugs"], twitch_client=client)
    print(streams)