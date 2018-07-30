"""
Modify text to be printed.
"""


from enum import Enum

RESET = "\33[0m"


class Color(Enum):
    """
    Text color options
    """
    BLACK = "\33[90m"
    RED = "\33[91m"
    GREEN = "\33[92m"
    YELLOW = "\33[93m"
    BLUE = "\33[94m"
    PINK = "\33[95m"
    CYAN = "\33[96m"
    WHITE = "\33[97m"

    def __str__(self):
        return self.value


class Style(Enum):
    """
    Text style options
    """
    BOLD = "\33[1m"
    ITALICS = "\33[3m"
    UNDERLINE = "\33[4m"
    INVERT = "\33[7m"
    CROSSOUT = "\33[9m"
    DOUBLE_UNDERLINE = "\33[21m"

    def __str__(self):
        return self.value


def color(text: str, color: Color) -> str:
    """
    Add color to a string.
    """
    return str(color) + text + RESET


def style(text: str, style: Style) -> str:
    """
    Add style to a string.
    """
    return str(style) + text + RESET


def modify(text: str, color: Color, style: Style) -> str:
    """
    Add color and style to a string.
    """
    return str(color) + str(style) + text + RESET
