from PIL import Image, ImageOps

def invert_scale_binary(image: Image, th: float, scale: float):
    w, h = image.width, image.height
    return ImageOps.invert(
        image.resize(size=(w * scale, h * scale)).convert("L").point(lambda p: 255 if p > th else 0)
    )
