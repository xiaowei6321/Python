import json
import pymysql

# 从JSON文件加载数据
with open('data.json','r',encoding='u8') as json_file:
    data = json.load(json_file)

# 连接到MySQL数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='test'
)

# 创建游标对象
cursor = conn.cursor()
# 选择数据库
cursor.execute('USE test')
# 清空test数据库
cursor.execute('DROP DATABASE IF EXISTS test')
# 创建test数据库
cursor.execute('CREATE DATABASE test')
# 选择数据库
cursor.execute('USE test')
# 创建用户表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        userId INT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        avatar VARCHAR(255)
    )
''')

# 创建帖子表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        postId INT PRIMARY KEY,
        title VARCHAR(255),
        content TEXT,
        userId INT,
        timestamp DATETIME,
        FOREIGN KEY (userId) REFERENCES users (userId)
    )
''')

# 创建点赞表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS likes (
        likeId INT PRIMARY KEY,
        userId INT,
        postId INT,
        FOREIGN KEY (userId) REFERENCES users (userId),
        FOREIGN KEY (postId) REFERENCES posts (postId)
    )
''')

# 创建转发表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shares (
        shareId INT PRIMARY KEY,
        userId INT,
        postId INT,
        FOREIGN KEY (userId) REFERENCES users (userId),
        FOREIGN KEY (postId) REFERENCES posts (postId)
    )
''')

# 创建评论表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        commentId INT PRIMARY KEY,
        userId INT,
        postId INT,
        content TEXT,
        FOREIGN KEY (userId) REFERENCES users (userId),
        FOREIGN KEY (postId) REFERENCES posts (postId)
    )
''')

# 插入用户数据
for user in data['users']:
    cursor.execute('''
        INSERT INTO users (userId, username, password, avatar)
        VALUES (%s, %s, %s, %s)
    ''', (user['userId'], user['username'], user['password'], user['avatar']))

# 插入帖子数据
for post in data['posts']:
    cursor.execute('''
        INSERT INTO posts (postId, title, content, userId, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    ''', (post['postId'], post['title'], post['content'], post['userId'], post['timestamp']))

# 插入点赞数据
for like in data['likes']:
    cursor.execute('''
        INSERT INTO likes (likeId, userId, postId)
        VALUES (%s, %s, %s)
    ''', (like['likeId'], like['userId'], like['postId']))

# 插入转发数据
for share in data['shares']:
    cursor.execute('''
        INSERT INTO shares (shareId, userId, postId)
        VALUES (%s, %s, %s)
    ''', (share['shareId'], share['userId'], share['postId']))

# 插入评论数据
for comment in data['comments']:
    cursor.execute('''
        INSERT INTO comments (commentId, userId, postId, content)
        VALUES (%s, %s, %s, %s)
    ''', (comment['commentId'], comment['userId'], comment['postId'], comment['content']))

# 提交更改
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
