# from context import pbn
from pathlib import Path

from pbn.tesseract_wrappers.image_to_text import image_to_text


def test_process_image():
    Path("./data/basic_text_images/hello.txt").unlink(missing_ok=True)
    Path("./data/basic_text_images/hello_processed.png").unlink(missing_ok=True)

    image_to_text("./data/basic_text_images/hello.png", save_output=True)

    assert Path("./data/basic_text_images/hello.png").exists()
    assert Path("./data/basic_text_images/hello.txt").exists()
    assert Path("./data/basic_text_images/hello_processed.png").exists()

    try:
        with open("./data/basic_text_images/hello.txt", "r") as file:
            data = file.read().replace('\n', '')
            assert data.strip() == "Hello! I am a test"
    except AssertionError as e:
        Path("./data/basic_text_images/hello.txt").unlink(missing_ok=True)
        Path("./data/basic_text_images/hello_processed.png").unlink(missing_ok=True)
        raise e

    Path("./data/basic_text_images/hello.txt").unlink(missing_ok=True)
    Path("./data/basic_text_images/hello_processed.png").unlink(missing_ok=True)


if __name__ == "__main__":
    test_process_image()
