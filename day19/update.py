import pymysql

db=pymysql.connect("localhost","root","root","pydb",charset="utf8")

cursor=db.cursor()

sql="update users set sex='女' where sex='赵六'"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()