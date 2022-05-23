import pytesseract

from os import path
from PIL import Image

def process_image(filename, preprocess = (lambda im: im), return_steps=False):
    absolute_filepath = path.abspath(filename)
    image_processed = preprocess(Image.open(absolute_filepath))
    image_processed_filepath = absolute_filepath.split(".")[0] + "_processed.png"
    image_processed.save(image_processed_filepath)
    image_text = pytesseract.image_to_string(image_processed)
    image_text_location = absolute_filepath.split(".")[0] + ".txt"
    with open(image_text_location, "w") as text_file:
        text_file.write(image_text)

    if return_steps:
        return {"image_processed": image_processed, "image_text": image_text}
