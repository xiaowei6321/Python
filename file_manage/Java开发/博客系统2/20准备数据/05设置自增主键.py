import mysql.connector

# 创建连接到数据库的连接器
cnx = mysql.connector.connect(user='root', password='123456',
                              host='127.0.0.1',
                              database='test')

# 创建一个新的游标
cursor = cnx.cursor()

table_names=['comments','likes','posts','shares','users']
table_id=['commentId','likeId','postId','shareId','userId']


for i in range(len(table_names)):
    table_name=table_names[i]
    table_id=table_id[i]
    # 执行ALTER TABLE命令，将'id'列修改为自增主键
    cursor.execute("ALTER TABLE "+table_name+" MODIFY COLUMN "+
                      table_id+" INT AUTO_INCREMENT  ")

# 执行ALTER TABLE命令，将'id'列修改为自增主键
# cursor.execute("ALTER TABLE your_table_name MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 提交到数据库执行
cnx.commit()

# 关闭游标和连接
cursor.close()
cnx.close()

