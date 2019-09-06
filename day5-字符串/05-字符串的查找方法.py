"""
1、字符串序列.find(子串， 查找开始位置下标， 查找结束位置下标)
    返回子串出现的初始下标
    1.1、rfind()函数查找方向和find()相反

2、字符串序列.index(子串， 查找开始位置下标， 查找结束位置下标)
    返回子串出现的初始下标
    2.1、rindex()函数查找方向和find()相反

3、字符串序列.count(子串， 查找开始位置下标， 查找结束位置下标)
    返回子串出现的次数
......
"""

myStr = 'hello world and itcast and itheima and Python'

# find() 函数
print(myStr.find('and'))  # 12
print(myStr.find('and', 15, 30))  # 23
print(myStr.find('ands'))  # 找不到返回-1

# index()函数
print(myStr.index('and'))  # 12
print(myStr.index('and', 15, 30))  # 23
# print(myStr.index('ands'))  # 找不到报错 substring not found

# count() 函数
print(myStr.count('and', 15, 30))  # 1
print(myStr.count('ands'))  # 0
