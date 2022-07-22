
from enum import Enum

class Size(Enum):
    SMALL = "SMALL"
    LARGE = "LARGE"
    TRAY = "TRAY"

class Color(Enum):
    RED = "RED"
    BLUE = "BLUE"

class Finish(Enum):
    GOLD = "GOLD"
    SILVER = "SILVER"


class Product():

    def __init__(self, size, color, finish):
        self.size = size
        self.color = color
        self.finish = finish