import twitch
import os

from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = twitch.TwitchHelix(
        client_id=os.getenv("twitch_api_client_id"),
        client_secret=os.getenv("twitch_api_client_secret"),
        scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS]
    )
    client.get_oauth()

    return client
