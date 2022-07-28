
from enum import Enum


class Product():

    def __init__(self, data):
        self.size = data["SIZE"]
        self.color = data["COLOR"]
        self.finish = data["FINISH"]

    def convert_to_json(self):
        product = {}
        product["SIZE"] = self.size.value
        product["COLOR"] = self.color.value
        product["FINISH"] = self.finish.value
        return product