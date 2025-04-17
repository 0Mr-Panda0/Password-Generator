import sqlite3
import os

# Create directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")
# Configure SQLite connection
db_path = "data/database.db"
db = sqlite3.connect(db_path, check_same_thread=False)

def create_table():
    cursor = db.cursor()
    # Creating table if not exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)"
    )
    db.commit()
    cursor.close()

def insert_password(password):
    cursor = db.cursor()
    cursor.execute("INSERT INTO password (password) VALUES (?)", (password,))
    db.commit()
    cursor.close()

def get_last_password():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM password ORDER BY id DESC LIMIT 1")
    password = cursor.fetchone()
    cursor.close()
    return password[1] if password else None

def delete_last_password():
    cursor = db.cursor()
    cursor.execute("DELETE FROM password ORDER BY id DESC LIMIT 1")
    db.commit()
    cursor.close()

