import pymysql

db = pymysql.connect(host='localhost', port=3306, password='', user='root', db='test')
cursor = db.cursor()

cursor.execute("SELECT * From test_table")
data = cursor.fetchall()

db.close()
for d in data:
    print(d)