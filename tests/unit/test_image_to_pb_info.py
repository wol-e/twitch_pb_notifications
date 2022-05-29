from pbn.stream_notifications import image_to_pb_info
from pbn.preprocess_image.preprocess import invert_scale_binary

def test_armada_ugs_1():
    filename = "./data/thumbnails/armadaugs_1653590651.png"
    pb_info = image_to_pb_info(
        filename=filename,
        preprocess=lambda im: invert_scale_binary(im, 100, 2)
    )
    pb_info["image_processed"].show()
    print(pb_info["pb_info"].lines)
    assert True

if __name__ == "__main__":
    test_armada_ugs_1()
