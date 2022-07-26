
from enum import Enum
from .product import Product

class Production_Status(Enum):
    INCOMPLETE = "INCOMPLETE",
    COMPLETE = "COMPLETE"

class Payment_Status(Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"


class Order():
    
    def __init__(self, data, new):

        self.first_name = data["FIRST_NAME"]
        self.last_name = data["LAST_NAME"]
        self.email = data["EMAIL"]
        self.products = [Product(product) for product in data["ORDER"]]

        if (new):
            self.production_status = Production_Status.INCOMPLETE
            self.payment_status = Payment_Status.UNPAID
        else:
            self.production_status = Production_Status(data["PRODUCTION_STATUS"])
            self.payment_status = Payment_Status(data["PAYMENT_STATUS"])


    def mark_order_as_complete(self):
        self.production_status = Production_Status.COMPLETE

    def mark_order_as_paid(self):
        self.payment_status = Payment_Status.PAID

    def convert_to_json(self):
        order_info = {}
        order_info["FIRST_NAME"] = self.first_name
        order_info["LAST_NAME"] = self.last_name
        order_info["EMAIL"] = self.email
        order_info["ORDER"] = [product.convert_to_json() for product in self.products]
        order_info["PRODUCTION_STATUS"] = self.production_status
        order_info["PAYMENT_STATUS"] = self.payment_status
        return order_info