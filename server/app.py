import initialize
from flask import Flask, jsonify, request, g
from flask_cors import CORS
import json
import sqlite3
import os
from config import DATABASE
from db_functions import initialize_users, initialize_posts, get_posts, get_single_post, get_comments, add_comment

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

        initialize_users(db)
        initialize_posts(db)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/get_all_posts', methods=['GET'])
def get_all_posts():
    try:
        return get_posts(get_db())
    except Exception as error:
        error_msg = f'Error: {error}'
        print(error_msg)
        return error_msg, 500


@app.route('/post/<int:post_id>', methods=['GET'])
def get_single_post_endpoint(post_id):
    try:
        if not post_id:
            return "Post ID is required", 400

        post = get_single_post(get_db(), post_id)

        if post is None:
            return "Post not found", 404

        comments = get_comments(get_db(), post_id)

        return jsonify({"post": post, "comments": comments})
    except Exception as error:
        error_msg = f'Error: {error}'
        print(error_msg)
        return error_msg, 500


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print('Initializing Database...')
        init_db()
        print('Initialized!')
    else:
        print('***')
    app.run(port=9988, debug=False)