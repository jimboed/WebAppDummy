

import base64
import flask
import json



app = flask.Flask(__name__)


@app.route('/integrationTest/test', methods=['GET'])
def add_message():




    return flask.request.args.get("val1")
    # return json.loads(flask.request.data)

@app.route('/')
def home():
    return "hello jimmmm"




if __name__ == '__main__':
    app.run(debug=True)
