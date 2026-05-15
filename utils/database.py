import sqlite3
import os

# =========================
# DATABASE PATH
# =========================

DB_FOLDER = "database"

DB_NAME = os.path.join(DB_FOLDER, "health.db")

# =========================
# CONNECT DATABASE
# =========================

def connect_db():

    # folder automatically create karega
    os.makedirs(DB_FOLDER, exist_ok=True)

    conn = sqlite3.connect(DB_NAME)

    return conn

# =========================
# CREATE TABLES
# =========================

def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    # USERS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    # HISTORY TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        disease TEXT,
        confidence REAL,
        symptoms TEXT
    )
    """)

    conn.commit()

    conn.close()