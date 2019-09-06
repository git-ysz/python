list1 = [10, 20, 30, 20, 40]
s1 = {100, 200, 300, 400}
t1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# 1、tuple():转换成元组
print(tuple(list1), tuple(s1))

# 2、list():转换成列表
print(list(s1), list(t1))

# 3、set():转换成集合 -- 去重
print(set(list1), set(t1))
