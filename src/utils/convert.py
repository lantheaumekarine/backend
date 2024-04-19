import PIL as pil


def resize_image(image, size):
    # Resize image to size
    return image.resize(size, pil.Image.ANTIALIAS)