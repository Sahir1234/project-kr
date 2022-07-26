
import email
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
    try:
        order = Order(request.json)
        id = order_manager.create_new_order(order, True)
        record_client.update_records(order_manager)
        email_client.send_customer_order_confirmation(id, order)
        email_client.send_admin_order_info(id, order)
        return jsonify( { "message" : "success" , "id" : id } )
    except RuntimeError as e:
        message = str(e)
        return jsonify( { "message" : message })


################################################################################


@app.route('/api/admin/cancel', methods = ['POST'])
def cancel_order():
    try:
        id = request.json["ORDER_ID"]
        order = order_manager.cancel_order(id)
        record_client.update_records(order_manager)
        email_client.send_customer_cancellation_confirmation(id, order)
        return jsonify( { "message" : "success" , "id" : id } )
    except RuntimeError as e:
        message = str(e)
        return jsonify( { "message" : message })


@app.route('/api/admin/paid', methods = ['POST'])
def mark_order_paid():
    try:
        id = request.json["ORDER_ID"]
        order = order_manager.mark_order_paid(id)
        record_client.update_records(order_manager)
        email_client.send_customer_payment_confirmation(id, order)
        return jsonify( { "message" : "success" , "id" : id } )
    except RuntimeError as e:
        message = str(e)
        return jsonify( { "message" : message })


@app.route('/api/admin/completed', methods = ['POST'])
def mark_order_completed():
    try:
        id = request.json["ORDER_ID"]
        order = order_manager.mark_order_produced(id)
        record_client.update_records(order_manager)
        email_client.send_customer_production_completion_confirmation(id, order)
        return jsonify( { "message" : "success" , "id" : id } )
    except RuntimeError as e:
        message = str(e)
        return jsonify( { "message" : message })


@app.route('/api/admin/close', methods = ['POST'])
def mark_order_closed():
    try:
        id = request.json["ORDER_ID"]
        order_manager.close_order(id)
        record_client.update_records(order_manager)
        return jsonify( { "message" : "success" , "id" : id } )
    except RuntimeError as e:
        message = str(e)
        return jsonify( { "message" : message })


################################################################################


if __name__ == '__main__':
    app.run()
