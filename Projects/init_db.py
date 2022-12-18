import sqlite3

conn = sqlite3.connect("database.db")

with open("init_db.sql", "r") as fr:
    conn.executescript(fr.read())

cur = conn.cursor()
cur.execute("INSERT INTO contents (title, content) VALUES ('First content.', 'OK')")

conn.commit()
conn.close()