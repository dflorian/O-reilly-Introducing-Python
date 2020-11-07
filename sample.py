import flask
from flask import request, jsonify


app = flask.Flask(__name__)


data = [
    {'id': 0,
     'name': 'Alice'
     },
    {'id': 1,
     'name': 'Bob'
     },
]


@app.route('/', methods=['GET'])
def main():
    return 'This is main'


@app.route('/api/name', methods=['GET'])
def get_name():
    try:
        id = int(request.args['id'])
        return data[id]
    except:
        return "no user found"


app.run()
