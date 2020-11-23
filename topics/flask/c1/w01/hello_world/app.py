from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/get-json')
def get_json():
    return jsonify({
        'key1': 'value1',
        'key2': 'value2'
    })


@app.route('/add-two-nums', methods=['POST'])
def add_two_nums():
    # Get x and y from posted data
    data_dict = request.get_json()

    # Add x and y
    x = data_dict["x"]
    y = data_dict["y"]
    z = x + y
    # Prepare a json

    return jsonify({
        "z":z
    }), 200

if __name__ == "__main__":
        app.run()