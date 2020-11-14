from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add', methods=['POST', 'GET'])
def add_route():
    return jsonify(
        test="test"
    )

app.run('', 8080)