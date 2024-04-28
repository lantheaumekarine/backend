import os
from PIL import Image

def resize_image(image_path, output_path, size):
    with Image.open(image_path) as image:
        # Resize image to size
        image.thumbnail(size)
        image.save(output_path)
    


def convert_jpg_to_webp(image_path, output_path):
    # Open the image file
    img = Image.open(image_path)
    # Save the image in WEBP format
    img.save(output_path, 'WEBP')
    # remove the image from image_path
    os.remove(image_path)
    

def tattoo_image(base_image_path, tattoo_image_path, output_path):
    # Open the base image
    base_image = Image.open(base_image_path)

    # find the position to paste the tattoo
    width, height = base_image.size
    position = ((width - 200)//2, (height - 200)//2)
    # Open the tattoo image
    tattoo_image = Image.open(tattoo_image_path)
    # Resize the tattoo image
    tattoo_image.thumbnail((200, 200))
    watermark = tattoo_image.copy()

    base_image.paste(tattoo_image, position, watermark)
    base_image.save(output_path)
    

