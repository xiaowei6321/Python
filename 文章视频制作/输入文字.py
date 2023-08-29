







# 读取章节.txt
with open('章节.txt', 'r', encoding='utf-8') as f:
    txt = f.read()


# 遍历加载数据
for i in txt.split('\n'):
    # 显示加载的数据
    print('加载的数据：', i)

