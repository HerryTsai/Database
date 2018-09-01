import pymysql

db = pymysql.connect(host='localhost', port=3306, password='', user='root', db='test')
cursor = db.cursor()

person_ = [['herry', 0, 48],
    ['judy', 1, 85],
    ['sam', 0, 29],
    ['jack', 0, 75],
    ['sandy', 1, 25]
]

i = 0
for person in person_:
    sql="insert into test_table(name, sex, score) value('"+person[0]+"',"+str(person[1])+","+str(person[2])+")"
    try:
        cursor.execute(sql)
        db.commit()
        print("第", (i), "筆資料已存入")
        i = i+1
    except:
        db.rollback()

db.close()