import json


def add_users(db, user_json='database/users.json'):
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
