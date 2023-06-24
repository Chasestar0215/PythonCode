from pymysql import Connection

con = Connection(  # 构建数据库连接
    host='localhost',
    port=3306,
    user='root',
    password='xiaojie.5212861'
)
# print(con.get_server_info())

cursor = con.cursor()  # 获取游标对象

con.select_db('student')  # 选择数据库

# sql = """update student set id = 20224301, name = 'John', age = 22, gender = 'male' where name = 'test'"""

cursor.execute("""select * from student""")
result: tuple = cursor.fetchall()

for i in result:
    print(i)

con.close()
