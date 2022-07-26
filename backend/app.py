
from flask import Flask, jsonify, request
from email_module.email_client import EmailClient
from records_module.record_client import RecordClient
from models.product import Product
from models.order import Order
from models.order_manager import OrderManager

app = Flask(__name__)
email_client = EmailClient()
record_client = RecordClient()
order_manager = OrderManager(record_client.read_records())


################################################################################


#
# THIS ROUTE THROWS AN ERROR IF THE ID CANNOT BE GENERATED, MUST CATCH
#
@app.route('/api/customer/order', methods = ['POST'])
def place_order():
    order = Order(request.json)
    id = order_manager.create_new_order(order, True)
    record_client.update_records(order_manager)
    email_client.send_order_confirmation(id, order)
    return jsonify( { "ORDER_ID" : id } )

################################################################################

@app.route('/api/admin/cancel', methods = ['POST'])
def cancel_order():

    order_id = request.json["ORDER_ID"]

    # cancel order
    # remove it from active orders
    # email cancellation confirmation
    # if paid, issue refund
    return 'cacncel ORDER'

@app.route('/api/admin/paid', methods = ['POST'])
def mark_order_paid():
    order_id = request.json["ORDER_ID"]
    # order has been paid for
    # wait for completion or if complete schedule pick up time
    return 'cacncel ORDER'

@app.route('/api/admin/completed', methods = ['POST'])
def mark_order_completed():
    order_id = request.json["ORDER_ID"]
    # order has been produced 
    # notify customer
    # schedule pick up time
    return 'cacncel ORDER'


@app.route('/api/admin/close', methods = ['POST'])
def mark_order_closed():
    order_id = request.json["ORDER_ID"]
    # when the order has been completed, paid for, and given to customer
    # everything i done so no need to see on website anymore
    return 'ccel ORDER'

################################################################################


if __name__ == '__main__':
    app.run()
