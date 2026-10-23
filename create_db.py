import sqlite3

conn = sqlite3.connect("events.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")