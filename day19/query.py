#数据库新增
import pymysql

#打开数据库连接
db=pymysql.connect("localhost","root","root","pydb",charset="utf8")
#使用cursor()方法获取操作游标
cursor=db.cursor()

sql="select * from users"
try:
    cursor.execute(sql)
    #获取所有记录列表
    results=cursor.fetchall()
    for row in results:
        name=row[0]
        sex=row[1]
        age=row[2]
        print("name=%s,sex=%s,age=%d"%(name,sex,age))
except:
    print("Error:unable to fetch data!")

#关闭数据库
db.close()