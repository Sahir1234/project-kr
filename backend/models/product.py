
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

    def __init__(self, data):
        self.size = Size(data["SIZE"])
        self.color = Color(data["COLOR"])
        self.finish = Finish(data["FINISH"])

    def convert_to_json(self):
        product = {}
        product["SIZE"] = self.size.value
        product["COLOR"] = self.color.value
        product["FINISH"] = self.finish.value
        return product