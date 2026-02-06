import sqlite3

conn = sqlite3.connect('first.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT ,
                   email TEXT
               )
               """)

conn.commit()
conn.close()

print("Database and table created successfully!")