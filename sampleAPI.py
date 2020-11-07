import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = [
    {'id': 0,
    'name': 'Alice'
    },
    {'id': 1,
    'name': 'Bob'
    },
]

@app.route('/', methods=['GET'])
def home():
    return 'API home'

@app.route('/api/v1/name', methods=['GET'])
def api_id():
    try:
        id = int(request.args['id'])
    except:
        return "no value available for this id"

    output = []
    for value in data:
        if id == value['id']:
            output.append(value['name'])

    return jsonify(output)

app.run()