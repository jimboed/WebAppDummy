 

import base64
import flask




app = flask.Flask(__name__)


@app.route('/integrationTest', methods=['GET'])
def add_message():
    content = request.get_json(silent=True)

    return content


@app.route('/')
def home():
    return "hello jim"




if __name__ == '__main__':
    app.run(debug=True)
