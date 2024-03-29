
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

        self.name = data["NAME"]
        self.email = data["EMAIL"]
        self.phone = data["PHONE"]
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
        order_info["NAME"] = self.name
        order_info["EMAIL"] = self.email
        order_info["PHONE"] = self.phone
        order_info["ORDER"] = [product.convert_to_json() for product in self.products]
        order_info["PRODUCTION_STATUS"] = self.production_status
        order_info["PAYMENT_STATUS"] = self.payment_status
        return order_info