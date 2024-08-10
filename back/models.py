import sqlite3

DATABASES = {
    'users': 'users.db',
    'books': 'books.db'
}

def connect_db(db_name):
    return sqlite3.connect(DATABASES[db_name])

def init_db():
    with connect_db('users') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

    with connect_db('books') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
