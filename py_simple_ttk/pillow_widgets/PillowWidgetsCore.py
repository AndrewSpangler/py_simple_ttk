from PIL import Image, ImageTk
from numpy import asarray
import io, os


def load_image_from_byte_array(byte_array: bytes):
    """Converts a png encoded in bytes to a PIL Image"""
    return Image.open(io.BytesIO(byte_array))


def load_tk_image_from_byte_array(byte_array: bytes):
    """Converts a png encoded in bytes to a TK Image"""
    return ImageTk.PhotoImage(load_image_from_byte_array(byte_array))


def convert_image_to_grayscale(image: Image) -> Image:
    return image.convert("LA")


def convert_image_to_blackandwhite(image: Image) -> Image:
    return image.convert("L").convert("1")
