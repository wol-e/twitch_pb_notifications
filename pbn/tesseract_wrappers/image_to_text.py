import pytesseract

from os import path
from PIL import Image

def image_to_text(filename, preprocess = (lambda im: im), save_output=False):
    """
    reads image file at filename and writes the preprocessed image and extracted text at same directory
    :param filename:
    :param preprocess:
    :param save_output:
    :return:
    """

    absolute_filepath = path.abspath(filename)
    image_processed = preprocess(Image.open(absolute_filepath))
    image_text = pytesseract.image_to_string(image_processed)

    if save_output:
        image_processed_filepath = absolute_filepath.rsplit(".", 1)[0] + "_processed.png"
        image_processed.save(image_processed_filepath)
        image_text_filepath = absolute_filepath.rsplit(".", 1)[0] + ".txt"
        with open(image_text_filepath, "w") as text_file:
            text_file.write(image_text)

    return {"image_processed": image_processed, "image_text": image_text}
