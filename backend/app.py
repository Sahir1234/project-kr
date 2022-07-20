from flask import Flask
from flask import jsonify

app = Flask(__name__)
    
# contact us
@app.route('/api/contact', methods = ['GET'])
def contact_us():
    return 'CONTACT US'
    
# place an order
@app.route('/api/order', methods = ['POST'])
def place_order():
    return 'PLACE ORDER'
    
# reroute invalid URLs
@app.errorhandler(404)
def page_not_found(e):
    return 'INVALID API CALL'


if __name__ == '__main__':
    app.run()
