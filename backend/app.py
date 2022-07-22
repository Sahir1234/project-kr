
from flask import Flask, jsonify
from email_module.email_client import EmailClient

app = Flask(__name__)
email_client = EmailClient()


################################################################################

@app.route('/api/customer/order', methods = ['POST'])
def place_order():
    # customer places order
    # create new record
    # send email confirmation to them and self
    return 'PLACE ORDER'

################################################################################

@app.route('/api/admin/modify', methods = ['POST'])
def modify_order():
    # change the existing order and mark it as incomplete if it is
    # email notification
    return 'modify ORDER'

@app.route('/api/admin/cancel', methods = ['POST'])
def cancel_order():
    # cancel order
    # remove it from active orders
    return 'cacncel ORDER'

@app.route('/api/admin/paid', methods = ['POST'])
def mark_order_paid():
    # order has been paid for
    # wait for completion or if complete schedule pick up time
    return 'cacncel ORDER'

@app.route('/api/admin/completed', methods = ['POST'])
def mark_order_completed():
    # order has been produced 
    # notify customer
    # schedule pick up time
    return 'cacncel ORDER'


@app.route('/api/admin/close', methods = ['POST'])
def mark_order_closed():
    # when the order has been completed, paid for, and given to customer
    # everything i done so no need to see on website anymore
    return 'cacncel ORDER'

################################################################################


if __name__ == '__main__':
    app.run()
