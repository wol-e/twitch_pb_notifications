import importlib

from .twitch_api.streams import get_stream, save_thumbnail
from .twitch_api.get_client import get_client
from .tesseract_wrappers.image_to_text import image_to_text
from .process_image_text.process import pb_info

def report_online(user_login, chat_id):
    """
    Reports to specified telegram chat when specified users come online
    :param user_logins:
    :param chat_id:
    :return: None
    """
    client = get_client()
    stream = get_stream(user_login=user_login, twitch_client=client)
    print(stream)
    # TODO
    pass


def report_pb_in_progress(user_login, directory, preprocess, return_steps=False):
    client = get_client()
    filename = save_thumbnail(user_login=user_login, twitch_client=client, directory=directory)
    tesseract_output = image_to_text(filename, preprocess=preprocess, return_steps=return_steps)
    extracted_text = tesseract_output["image_text"]

    # check if there is a user specific extraction class
    user_extraction_class_module = "pbn.process_image_text.user_fits." + user_login
    user_module_spec = importlib.util.find_spec(user_extraction_class_module)
    if user_module_spec:
        user_fit = importlib.import_module(user_extraction_class_module)

    else:
        return

    pb_extraction = user_fit.PBInfoUser(extracted_text)
    if pb_extraction.is_pb_pace:
        print("hurray")