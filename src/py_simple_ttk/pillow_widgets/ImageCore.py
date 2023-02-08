import io
from PIL import Image, ImageTk, ImageDraw


def load_image_from_byte_array(byte_array: bytes) -> Image.Image:
    """Converts a png encoded in bytes to a PIL Image"""
    return Image.open(io.BytesIO(byte_array))


def load_tk_image_from_bytes_array(bytes_array: bytes) -> ImageTk.PhotoImage:
    """Loads a png encoded in bytes to an image tkinter can process"""
    return ImageTk.PhotoImage(load_image_from_byte_array(bytes_array))


def convert_image_to_grayscale(image: Image.Image) -> Image.Image:
    """Converts a PIL image to grayscale"""
    return image.convert("LA")


def convert_image_to_blackandwhite(image: Image.Image) -> Image.Image:
    """Converts an image to black and white"""
    return image.convert("L").convert("1")


def make_checkerboard(
    width: int,
    height: int,
    repeat: int = 14,
    color_1: tuple = (127, 127, 127, 255),
    color_2: tuple = (64, 64, 64, 255),
) -> Image.Image:
    """Function to make a background checkerboard for displaying images on"""
    image = Image.new("RGBA", (width, height), color_1)
    draw = ImageDraw.Draw(image)
    for x in range((width // repeat) + 1):
        for y in range((height // repeat) + 1):
            if (x + y) % 2:
                draw.rectangle(
                    (x * repeat, y * repeat, (x + 1) * repeat, (y + 1) * repeat),
                    fill=color_2,
                )
    return image
