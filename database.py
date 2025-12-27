import sqlite3

conn = sqlite3.connect("road.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS detections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    object_type TEXT,
    confidence REAL,
    timestamp TEXT,
    latitude REAL,
    longitude REAL
)
""")

conn.commit()
conn.close()

print("✅ Database and table created successfully.")
