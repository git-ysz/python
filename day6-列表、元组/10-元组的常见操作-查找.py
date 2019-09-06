"""
1、index()
2、count()
3、len()
"""
t1 = ('aa', 'bb', 'bb', 'cc', 'dd')
# 下标
print(t1[0])  # 返回下标所在数据

# index
print(t1.index('bb'))  # 返回下标
# print(t1.index('bbb'))  # 报错

# count 统计某个数据出现的次数
print(t1.count('bb'))

# len
print(len(t1))
