import sqlite3

conn = sqlite3.connect('test.db')
db = conn.cursor()

person = db.execute("SELECT id, name, score from test_table")
for p in person:
    print("id: "+str(p[0])+" name: "+p[1]+" score: "+str(p[2]))

conn.close()