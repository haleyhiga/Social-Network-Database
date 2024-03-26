import os
import sys
import sqlite3
from main import DB_FILE

def getDatabase(create=False):
    if os.path.exists(DB_FILE):
        if create:
            os.remove(DB_FILE)
    else:
        if not create:
            print("No database has been discovered.")
            sys.exit(1)
    
    con = sqlite3.connect(DB_FILE)
    con.execute('PRAGMA foreign_keys = ON')
    return con

def createDatabase():
    with getDatabase(create = True) as con:
        # might need to look back on for delete on cascade

        # Users
        con.execute('''
CREATE TABLE users (
    user_id             INTEGER PRIMARY KEY,
    email               TEXT NOT NULL UNIQUE
)
''')
        # Accounts
        con.execute('''
CREATE TABLE accounts (
    account_id          INTEGER PRIMARY KEY,
    user_id             INTEGER NOT NULL,
    username            TEXT NOT NULL UNIQUE,
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
''')
        # Followers
        con.execute('''
CREATE TABLE followers (
    username            TEXT,
    follower_username   TEXT,
    FOREIGN KEY(username) REFERENCES accounts(username) ON DELETE CASCADE,
    FOREIGN KEY(follower_username) REFERENCES accounts(username) ON DELETE CASCADE
)
''')
        # Posts
        con.execute('''
CREATE TABLE posts (
    username            TEXT,
    post_id             INTEGER PRIMARY KEY,
    post_message        TEXT,
    time_published      DEFAULT CURRENT_TIMESTAMP,
    time_editted        DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(username) REFERENCES accounts(username) ON DELETE CASCADE
)
''')
        # Block Accounts
        con.execute('''
CREATE TABLE blocked_accounts (
    username            TEXT,
    blocked_username    TEXT,
    FOREIGN KEY(username) REFERENCES accounts(username) ON DELETE CASCADE,
    FOREIGN KEY(blocked_username) REFERENCES accounts(username) ON DELETE CASCADE
)
''')
        # Likes and Dislikes
        con.execute('''
CREATE TABLE likes_dislikes (
    post_id             INTEGER,
    username            TEXT,
    liked               INTEGER,
    FOREIGN KEY(post_id) REFERENCES posts(post_id) ON DELETE CASCADE,
    FOREIGN KEY(username) REFERENCES accounts(username) ON DELETE CASCADE
)
''')
        
    print("Database has been successfully created.")
    con.commit()