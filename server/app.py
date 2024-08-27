import initialize
from flask import Flask, jsonify, g
from flask_cors import CORS
import json
import sqlite3
import os
from config import DATABASE
from db_functions import add_users

app = Flask(__name__)
CORS(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(os.path.join('database', 'schema.sql'), mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

        add_users(db)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


data = {}
with open('testing_files/api_data_partial.json') as f:
    data = json.load(f)


@app.route('/get_news', methods=['GET'])
def get_data():
    global data
    return jsonify(data)


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print('Initializing Database...')
        init_db()
        print('Initialized!')

    app.run(port=9988, debug=False)
