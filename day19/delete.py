import pymysql

db=pymysql.connect("localhost","root","root","pydb",charset="utf8")
cursor=db.cursor()
sql="delete from users where name='张三'"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
