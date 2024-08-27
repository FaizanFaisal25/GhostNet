import json
import random
from datetime import datetime


def initialize_users(db, user_json='database/users.json'):
    with open(user_json) as f:
        user_data = json.load(f)

    cursor = db.cursor()

    insert_query = '''
        INSERT INTO users (name, dob, location, bio)
        VALUES (?, ?, ?, ?)
    '''

    for user in user_data:
        cursor.execute(insert_query, (
            user.get('name'),
            user.get('dob'),
            user.get('location'),
            user.get('bio'),
        ))

    db.commit()

    print('Users Initialized!')


def initialize_posts(db, post_json='testing_files/api_data_partial.json'):
    with open(post_json) as f:
        post_data = json.load(f)['articles']

    cursor = db.cursor()

    cursor.execute("SELECT id FROM users")
    author_ids = cursor.fetchall()
    author_ids = [_id[0] for _id in author_ids]

    insert_query = '''
        INSERT INTO posts (source_id, source_name, author, title, description, url, url_to_image, published_at, content)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    for post in post_data:
        author_id = random.choice(author_ids)

        cursor.execute(insert_query, (
            post['source']['id'],
            post['source']['name'],
            author_id,
            post['title'],
            post.get('description', ''),
            post.get('url', ''),
            post.get('urlToImage', ''),
            post['publishedAt'],
            post['content']
        ))

    db.commit()

    print('Posts Initialized!')


def get_posts(db):
    cursor = db.cursor()

    select_query = '''
    SELECT
        posts.id AS post_id,
        posts.source_id,
        posts.source_name,
        posts.author AS author_id,
        posts.title,
        posts.description,
        posts.url,
        posts.url_to_image,
        posts.published_at,
        posts.content,
        users.name AS author_name,
        users.profile_photo AS author_profile_photo
    FROM
        posts
    JOIN
        users
    ON
        posts.author = users.id
    '''

    cursor.execute(select_query)
    items = cursor.fetchall()

    posts = []

    for item in items:
        post = {
            "id": item[0],
            "source_id": item[1],
            "source_name": item[2],
            "author_id": item[3],
            "author_name": item[10],
            "author_profile_photo": item[11],
            "title": item[4],
            "description": item[5],
            "url": item[6],
            "url_to_image": item[7],
            "published_at": item[8],
            "content": item[9]
        }

        posts.append(post)

    return posts


def get_single_post(db, post_id):
    pass


def add_comment(db, post_id, author_id, content):
    cursor = db.cursor()

    published_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    insert_query = '''
        INSERT INTO comments (post_id, author, content, published_at)
        VALUES (?, ?, ?, ?)
    '''

    cursor.execute(insert_query, (post_id, author_id, content, published_at))

    db.commit()


def get_comments(db, post_id):
    cursor = db.cursor()

    select_query = '''
    SELECT
        comments.id AS comment_id,
        comments.content,
        comments.published_at,
        users.name AS author_name,
        users.profile_photo AS author_profile_photo
    FROM
        comments
    JOIN
        users
    ON
        comments.author = users.id
    WHERE
        comments.post_id = ?
    '''

    cursor.execute(select_query, (post_id,))
    items = cursor.fetchall()

    comments = []

    for item in items:
        comment = {
            "id": item[0],
            "content": item[1],
            "published_at": item[2],
            "author_name": item[3],
            "author_profile_photo": item[4]
        }

        comments.append(comment)

    return comments
