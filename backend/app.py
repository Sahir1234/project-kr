
from flask import Flask
from flask import jsonify

from email_module.email_client import EmailClient

app = Flask(__name__)
    
# contact us
@app.route('/api/contact', methods = ['GET'])
def contact_us():
    return 'CONTACT US'
    
# place an order
@app.route('/api/order', methods = ['GET'])
def place_order():
    # EmailClient.send()
    return 'PLACE ORDER'
    
# reroute invalid URLs
@app.errorhandler(404)
def page_not_found(e):
    return 'INVALID API CALL'


if __name__ == '__main__':
    app.run()
