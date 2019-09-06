str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (10, 20, 30, 40)
s1 = {10, 20, 30, 40}
dict1 = {'name': 'Tom', 'age': 20}

# 1、len() --》 获取长度
print(
    len(str1),
    len(list1),
    len(t1),
    len(s1),
    len(dict1),
    len(dict1.keys()),
    len(dict1.values())
)

# 2、del 或 del() 删除目标
del str1  # 或者 del(str1)
# print(str1)  # 已删除
del list1[0]
print(list1)
del t1
# print(t1)  # 已删除
del s1
# print(s1)  # 已删除
del dict1['name']
print(dict1)

# 3、max,min ==> 最大值，最小值
str2 = 'abcdefg'
list2 = [10, 20, 30, 40]
print(max(str2), max(list2))
print(min(str2), min(list2))

# 4、range(start, end, step) --> 生成start到end的数字，步长为step，供循环使用
print(range(1, 10, 1), list(range(1, 10, 1)), tuple(range(1, 10, 1)), set(range(1, 10, 1)))
print(range(1, 10, 2), list(range(1, 10, 2)))
print(range(5), list(range(5)))

for i in range(5, 10):
    print(i)

# 5、enumerate(可遍历对象, start=0) --> start开始下标
"""
返回结果为下标对应值的元组
"""
print(list(enumerate(list1)))

for i in enumerate(list1, start=1):
    print(i)
