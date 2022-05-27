from pbn.twitch_api.streams import get_stream
from pbn.twitch_api.get_client import get_client

if __name__ == "__main__":
    client = get_client()
    streams = get_stream(user_logins=["wilko"], twitch_client=client)
    print(streams)