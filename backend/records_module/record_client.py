
import json

class RecordClient():
    
    def __init__(self):
        self.file = "./email_module/order_records.json"

    def read_records(self):
        file = open("./email_module/order_records.json", "r")
        records = json.load(file)
        file.close()
        return records

    def update_records(self, order_manager):
        file = open("./email_module/order_records.json", "w+")
        json.dump(order_manager.convert_to_json(), file)
        file.close()     
