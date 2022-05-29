import importlib

from .twitch_api.streams import get_stream, save_thumbnail
from .twitch_api.get_client import get_client
from .tesseract_wrappers.image_to_text import image_to_text

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


def image_to_pb_info(filename, pb_extraction_method_name="generic", preprocess=lambda im: im, save_output=False):
    tesseract_output = image_to_text(filename, preprocess=preprocess, save_output=save_output)
    image_processed = tesseract_output["image_processed"]
    extracted_text = tesseract_output["image_text"]

    if pb_extraction_method_name != "generic":
        user_extraction_class_module = "pbn.process_image_text.user_fits." + pb_extraction_method_name
        user_module_spec = importlib.util.find_spec(user_extraction_class_module)
        if user_module_spec:
            print(f"Info: Using extraction method for user {pb_extraction_method_name}")
            extraction_lib = importlib.import_module(user_extraction_class_module)
        else:
            print("Falling back to generic pb extraction method for lack of user specific one...")
            extraction_lib = importlib.import_module("pbn.process_image_text.generic")

    else:
        extraction_lib = importlib.import_module("pbn.process_image_text.generic")

    PBInfo = extraction_lib.PBInfo
    pb_extraction = PBInfo(extracted_text)

    return {"pb_info": pb_extraction, "image_processed": image_processed}



def report_pb_in_progress(user_login, directory, preprocess, try_user_fit=False):
    client = get_client()
    filename = save_thumbnail(user_login=user_login, twitch_client=client, directory=directory)

    pb_extraction = image_to_pb_info(
        filename,
        pb_extraction_method_name=("generic" if not try_user_fit else user_login),
        preprocess=preprocess
    )["pb_info"]

    if pb_extraction.is_pb_pace:
        print("We're on pb pace!")

    else:
        print("Nothing unusual...")
