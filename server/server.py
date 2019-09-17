from flask import flask


app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong!'
