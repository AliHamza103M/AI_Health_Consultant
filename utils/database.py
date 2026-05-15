import sqlite3

# =========================
# DATABASE NAME
# =========================

DB_NAME = "database/health.db"

# =========================
# CONNECT DATABASE
# =========================

def connect_db():

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

        username TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL
    )
    """)

    # PREDICTION HISTORY TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        disease TEXT,

        confidence REAL,

        symptoms TEXT,

        prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()

    print("Database tables created successfully.")