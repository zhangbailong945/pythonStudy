#数据库新增
import pymysql

#打开数据库连接
db=pymysql.connect("localhost","root","root","pydb",charset="utf8")
#使用cursor()方法获取操作游标
cursor=db.cursor()

#SQL语句插入
sql="insert into users(name,sex,age)values('王五','赵六',20)"

try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    db.rollback()

#关闭数据库连接
db.close()

