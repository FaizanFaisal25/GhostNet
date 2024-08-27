import json
import random


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

    select_query = f"SELECT * FROM posts"
    cursor.execute(select_query)
    items = cursor.fetchall()

    posts = []

    for item in items:
        post = {
            "id": item[0],
            "source_id": item[1],
            "source_name": item[2],
            "author_id": item[3],
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
    cursor = db.cursor()

    select_query = '''
        SELECT p.id, p.source_id, p.source_name, p.author, p.title, p.description, 
               p.url, p.url_to_image, p.published_at, p.content,
               u.name, u.dob, u.location, u.bio, u.profile_photo
        FROM posts p
        JOIN users u ON p.author = u.id
        WHERE p.id = ?
    '''
    cursor.execute(select_query, (post_id,))

    item = cursor.fetchone()

    if item is None:
        return None
    
    post = {
        "id": item[0],
        "source_id": item[1],
        "source_name": item[2],
        "author_id": item[3],
        "title": item[4],
        "description": item[5],
        "url": item[6],
        "url_to_image": item[7],
        "published_at": item[8],
        "content": item[9],
        "author": {
            "name": item[10],
            "dob": item[11],
            "location": item[12],
            "bio": item[13],
            "profile_photo": item[14]
        }
    }

    return post
