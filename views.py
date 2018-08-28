 
import base64
import flask

from init import app, db
import models



@app.route('/integrationTest', methods=['GET'])
def add_message():
    content = request.get_json(silent=True)

    return content


@app.route('/')
def home():
    return "hello jim"
