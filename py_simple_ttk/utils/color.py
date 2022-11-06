def reduce_255(in_value: int, maxval: int = 255) -> int:
    """Limits a val to a range of 0 to 255"""
    return max(0, min(in_value, maxval))


def rgb_to_hex(rgb: tuple) -> str:
    """Converts an rgb tuple to hex"""
    return "#{0:02x}{1:02x}{2:02x}".format(
        reduce_255(rgb[0]), reduce_255(rgb[1]), reduce_255(rgb[2])
    )


def rgba_to_hex(rgba: tuple) -> str:
    """Converts an rgba tuple to rgba hex"""
    return "#{0:02x}{1:02x}{2:02x}{3:02x}".format(
        reduce_255(rgba[0]),
        reduce_255(rgba[1]),
        reduce_255(rgba[2]),
        reduce_255(rgba[3]),
    )


def hex_to_rgb(hex: str) -> tuple:
    """Converts hex to rgb tuple"""
    return (int(hex[i : i + 2], 16) for i in range(1, 6, 2))


def hex_to_rgba(hex: str) -> tuple:
    """Tries to convert rgba hex to rgba, on failure converts rgb hex to rgb and sets a full opacity"""
    try:
        return (int(hex[i : i + 2], 16) for i in range(1, 8, 2))
    except ValueError as e:
        return (*hex_to_rgb(hex), 255)


def get_gradient(steps: int) -> tuple:
    """Generates a black / white gradient with a given number of steps"""
    return (
        rgb_to_hex(v) for v in reversed(linear_gradient("#FFFFFF", "#000000", steps))
    )


def rgb_to_scalar(rgb: tuple) -> tuple:
    """Converts an rgb itterable to scalar list"""
    return (int(x / 255.0) for x in rgb)


def scalar_to_rgb(rgb: tuple) -> tuple:
    """Converts rgb scalar to rgb list"""
    return (int(x * 255.0) for x in rgb)


def linear_gradient(
    start_hex: str = "#000000", finish_hex: str = "#FFFFFF", n: int = 10
) -> list:
    """Generates a linear gradient between two colors, accepts html hex or rgb formats"""
    s = hex_to_rgb(start_hex) if isinstance(start_hex, str) else start_hex
    f = hex_to_rgb(finish_hex) if isinstance(finish_hex, str) else finish_hex
    rgb = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        rgb.append([int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)])
    return rgb


def get_rainbow(steps: int) -> tuple:
    """Generates a rainbow with a given number of steps. Steps must be divisible by 4)"""
    rainbow = [linear_gradient("#FF0000", "#FFFF00", step := int(steps / 4))]
    rainbow.extend(linear_gradient("#7FFF00", "#00FF7F", step))
    rainbow.extend(linear_gradient("#00FFF", "#0000FF", step))
    rainbow.extend(linear_gradient("#7F00FF", "#FF007f", step))
    return (rgb_to_hex(v) for v in reversed(rainbow))


def needs_white_text(color: str, barrier: int = 384) -> bool:
    """Returns True if luminance is under 50%"""
    if isinstance(color, str):
        if color.startswith("#"):
            if len(color) == 7:
                return sum(hex_to_rgb(color)) < barrier
            elif len(color) == 9:
                return sum(hex_to_rgba(color)[:3]) < barrier
    elif isinstance(color, list) or isinstance(color, tuple):
        if len(color) == 3:
            return sum(color) < barrier
        elif len(color) == 4:
            return sum(color) < barrier
    ValueError(f"Invalid color {color}")
