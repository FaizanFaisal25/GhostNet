from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/get_news', methods=['GET'])
def get_data():
    with open('api_data.json') as f:
        data = json.load(f)
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=9988, debug=False)
