from flask import Flask
from flask import render_template
from flask import jsonify
from flask import url_for
from flask import redirect

app = Flask(__name__)

####################################################

# main page
@app.route('/')
def home():
    return render_template('index.html')

####################################################

# api home
@app.route('/api')
def api():
    return 'Hey! You should not be here!'

####################################################
    
# reroute invalid URLs
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')
    
####################################################

if __name__ == '__main__':
    app.run()
