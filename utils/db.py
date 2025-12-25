import sqlite3
import hashlib
import os

DB_FILE = "data/users.db"

def _get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = _get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def _hash_password(password: str) -> str:
    # Use a fixed salt for simplicity in this demo, but ideally use random salt per user
    salt = "somesalt" 
    return hashlib.sha256((password + salt).encode()).hexdigest()

def create_user(email, password, name):
    try:
        conn = _get_connection()
        c = conn.cursor()
        hashed = _hash_password(password)
        c.execute("INSERT INTO users (email, name, password_hash) VALUES (?, ?, ?)", 
                  (email, name, hashed))
        conn.commit()
        conn.close()
        return True, "User created successfully"
    except sqlite3.IntegrityError:
        return False, "Email already exists"
    except Exception as e:
        return False, str(e)

def verify_user(email, password):
    conn = _get_connection()
    c = conn.cursor()
    hashed = _hash_password(password)
    c.execute("SELECT * FROM users WHERE email = ? AND password_hash = ?", (email, hashed))
    user = c.fetchone()
    conn.close()
    
    if user:
        return {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"]
        }
    return None

# Initialize on module load
init_db()
