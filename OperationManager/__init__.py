import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库连接
db = pymysql.connect("47.95.231.82", "manager", "manager123", "operation")

# 使用cursor()操作游标
cursor = db.cursor()

# 执行sql
cursor.execute("SELECT VERSION()")

# 使用fetcone()方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库
cursor.close()

# 添加部分注解