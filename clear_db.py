# clear_db.py

import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM events")

conn.commit()
conn.close()

print("Database Cleared!")