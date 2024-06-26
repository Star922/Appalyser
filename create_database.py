import sqlite3

def setup_userdb():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Create users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        searchRetries INTEGER NOT NULL,
        summaryRetries INTEGER NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

def setup_commdb():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Create users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        comment TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

if __name__=='__main__':
    setup_commdb()
