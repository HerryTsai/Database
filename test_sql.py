import sqlite3

conn = sqlite3.connect('test.db')
db = conn.cursor()
db.execute("CREATE TABLE test_table(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, score INTEGER NOT NULL);")
conn.commit()

person = [[1, "jack", 80],
    [2, "king", 46],
    [3, "jeff", 59]]
for p in person:
    db.execute("INSERT INTO test_table(id, name, score) VALUES("+str(p[0])+",'"+p[1]+"',"+str(p[2])+")")
conn.commit()
conn.close()