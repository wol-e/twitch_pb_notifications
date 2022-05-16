#from context import pbn
from pathlib import Path

from pbn.tesseract_functions.process_image import process_image

def test_process_image():
    Path("./data/hello.txt").unlink(missing_ok=True)
    Path("./data/hello_processed.png").unlink(missing_ok=True)

    process_image("./data/hello.png")

    assert Path("./data/hello.png").exists()
    assert Path("./data/hello.txt").exists()
    assert Path("./data/hello_processed.png").exists()

    with open("./data/hello.txt", "r") as file:
        data = file.read().replace('\n', '')
        assert data.strip() == "Hello! I am a test."

if __name__ == "__main__":
    test_process_image()
