

import base64
import flask




app = flask.Flask(__name__)


@app.route('/integrationTest', methods=['GET'])
def add_message():

     

    return request.args


@app.route('/')
def home():
    return "hello jim"




if __name__ == '__main__':
    app.run(debug=True)
