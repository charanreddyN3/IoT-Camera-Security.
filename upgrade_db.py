import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

try:
    cursor.execute(
        "ALTER TABLE events ADD COLUMN image_path TEXT"
    )

    print("image_path column added successfully!")

except sqlite3.OperationalError:
    print("image_path column already exists!")

conn.commit()
conn.close()