
import string
import random
from .order import Order

class OrderManager():
    
    def __init__(self, records):

        self.orders = {"ACTIVE" : {}, "COMPLETED" : {}, "CANCELLED" : {}}
        for key in self.orders.keys():
            for id in records[key].keys():
                self.orders[key][id] = Order(records[key][id], False)


    def generate_new_order_id(self):
        tries = 0
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        while (id in self.orders["ACTIVE"].keys()):
            tries += 1
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if (tries == 15):
                raise RuntimeError("COULD NOT GENERATE A NEW ORDER ID!")
        self.orders["ACTIVE"][id] = {}
        return id


    def create_new_order(self, order):
        id = self.generate_new_order_id()
        self.orders["ACTIVE"][id] = order
        return id
        

    def convert_to_json(self):
        records = {}
        for key in self.orders.keys():
            records[key] = {}
            for id in self.orders[key].keys():
                records[key][id] = self.orders[key][id].convert_to_json()
        return records