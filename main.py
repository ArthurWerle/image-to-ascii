import sys
import os
from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100, height_ratio=0.55):
    """Resize image with an adjusted height to avoid stretching."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * height_ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    """Convert image to grayscale."""
    return image.convert("L")

def map_pixels_to_ascii_chars(image, range_width=25):
    """Map each pixel to an ASCII character based on brightness."""
    pixels = np.array(image)
    ascii_str = ""
    for pixel_value in pixels.flatten():
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100, height_ratio=0.55):
    """Convert an image to ASCII art with a height ratio adjustment."""
    image = Image.open(image_path)
    image = resize_image(image, new_width=new_width, height_ratio=height_ratio)
    image = grayscale_image(image)

    ascii_str = map_pixels_to_ascii_chars(image)
    img_width = image.width
    ascii_img = "\n".join(ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width))

    return ascii_img

def save_ascii_art(ascii_img, image_path):
    """Save the ASCII art to a text file with a name based on the original file."""
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f"{base_name}_ascii.txt"
    with open(output_path, "w") as f:
        f.write(ascii_img)
    print(f"ASCII art saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ascii_art.py <image_path> [new_width]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    new_width = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    ascii_img = convert_image_to_ascii(image_path, new_width=new_width, height_ratio=0.55)
    save_ascii_art(ascii_img, image_path)
    print(ascii_img)
