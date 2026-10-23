import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE events
SET image_path='static/evidence/event_1781378056.jpg'
WHERE id=542
""")

cursor.execute("""
UPDATE events
SET image_path='static/evidence/event_1781378066.jpg'
WHERE id=543
""")

conn.commit()
conn.close()

print("Updated Successfully")