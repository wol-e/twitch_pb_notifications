from pbn.stream_notifications import report_pb_in_progress
from pbn.preprocess_image.preprocess import invert_scale_binary


def preprocess(im):
    return invert_scale_binary(image=im, th=120, scale=2)


if __name__ == "__main__":
    report_pb_in_progress(
        user_login="wilko",
        directory="./data",
        preprocess=preprocess,
        return_steps=True
    )