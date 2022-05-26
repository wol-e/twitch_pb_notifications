from .twitch_api.streams import get_streams, save_thumbnail
from .twitch_api.get_client import get_client
from .tesseract_wrappers.image_to_text import image_to_text


def report_online(user_logins, chat_id):
    """
    Reports to specified telegram chat when specified users come online
    :param user_logins:
    :param chat_id:
    :return: None
    """
    client = get_client()
    streams = get_streams(user_logins=user_logins, twitch_client=client)
    print(streams)
    # TODO
    pass


def report_pb_in_progress(user_logins, directory, preprocess, return_steps=False):
    client = get_client()
    filenames = save_thumbnail(user_logins=user_logins, twitch_client=client, directory=directory)
    returns = [image_to_text(filename, preprocess=preprocess, return_steps=return_steps) for filename in filenames]
    if return_steps:
        return returns
