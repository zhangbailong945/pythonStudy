#创建数据库表
import pymysql
#打开数据库连接
db=pymysql.connect("localhost","root","root","pydb")
#使用cursor()方法创建一个游标对象cursor
cursor=db.cursor()
#使用execute()方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS USERS")
#是用预处理语句创建表
sql="""CREATE TABLE USERS(
    name varchar(30),
    sex int,
    age int
)"""

cursor.execute(sql)

db.close()

