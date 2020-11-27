from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB

UserNum = db['UserNum']

UserNum.insert({
    'num_of_user': 0
})

class Visit(Resource):
    def get(self):
        
        print(f'Visit Resource')
        prev_num = UserNum.find({})[0]['num_users']
        new_num = prev_num + 1
        UserNum.update({}, {
            "$set": {
                "num_of_users": new_num
            }
        })
        return str("Hello user " + str(new_num))

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


def validate_input(posted_data, method_name):
    print(posted_data)
    if((method_name == 'Add') or (method_name == 'Multiply') or (method_name == 'Subtract')):
        if('x' not in posted_data or 'y' not in posted_data):
            return 301
        else:
            return 200
    
    if(method_name == 'Divide'):
        if('x' not in posted_data or 'y' not in posted_data):
            return 301
        elif(int(posted_data['y']) == 0):
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = validate_input(posted_data, 'Add')
        if(status_code != 200):
            return jsonify({
            "Message": "Input Error",
            "Status Code": status_code
        })

        # Add x and y
        x = posted_data["x"]
        y = posted_data["y"]
        z = int(x) + int(y)
        # Prepare a json

        return jsonify({
            "Message":z,
            "Status Code": status_code
        })#, 200

    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass


class Subtract(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = validate_input(posted_data, 'Subtract')
        if(status_code != 200):
            return jsonify({
            "Message": "Input Error",
            "Status Code": status_code
        })

        # Add x and y
        x = posted_data["x"]
        y = posted_data["y"]
        z = int(x) - int(y)
        # Prepare a json

        return jsonify({
            "Message":z,
            "Status Code": status_code
        })#, 200

class Multiply(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = validate_input(posted_data, 'Multiply')
        if(status_code != 200):
            return jsonify({
            "Message": "Input Error",
            "Status Code": status_code
        })

        # Add x and y
        x = posted_data["x"]
        y = posted_data["y"]
        z = int(x) * int(y)
        # Prepare a json

        return jsonify({
            "Message":z,
            "Status Code": status_code
        })#, 200

class Divide(Resource):
    def post(self):
        posted_data = request.get_json()

        status_code = validate_input(posted_data, 'Divide')
        if(status_code != 200):
            return jsonify({
            "Message": "Input Error",
            "Status Code": status_code
        })

        # Add x and y
        x = posted_data["x"]
        y = posted_data["y"]
        z = int(x) / int(y)
        # Prepare a json

        return jsonify({
            "Message":z,
            "Status Code": status_code
        })#, 200


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/sub')
api.add_resource(Multiply, '/mul')
api.add_resource(Divide, '/div')
api.add_resource(Visit, '/hello')

if __name__ == "__main__":
        app.run(host="0.0.0.0")