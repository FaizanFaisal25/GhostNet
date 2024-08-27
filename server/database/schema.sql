CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob DATE,
    location TEXT,
    bio TEXT,
    profile_photo TEXT
);


CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id TEXT,
    source_name TEXT,
    author INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    url TEXT,
    url_to_image TEXT,
    published_at DATE NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (author) REFERENCES users (id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    author INTEGER NOT NULL,
    content TEXT NOT NULL,
    published_at DATE NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (author) REFERENCES users (id) ON DELETE CASCADE
);
