from pbn.stream_notifications import report_pb_in_progress
from pbn.preprocess_image.preprocess import invert_scale_binary


def preprocess(im):
    return invert_scale_binary(image=im, th=100, scale=2)


if __name__ == "__main__":
    report_pb_in_progress(
        user_login="weegee",
        directory="./data",
        preprocess=preprocess,
        try_user_fit=True,
    )