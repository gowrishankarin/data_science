from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

    if __name__ == "__main__":
        app.run()

@app.route('/get-json')
def get_json():
    return jsonify({
        'key1': 'value1',
        'key2': 'value2'
    })