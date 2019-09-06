s1 = {10, 20, 30}

# 1、remove(), 删除指定数据，没有则报错
s1.remove(10)
print(s1)
# s1.remove(100)  # 报错

# 2、discard()，删除指定数据，没有不报错
s1.discard(20)
print(s1)
s1.discard(100)  # 删除没有的数据不会报错
print(s1)

# 3、pop()，随机删除某个数据,并返回这个数据
s2 = {10, 20, 30, 40, 50, 60}
num = s2.pop()
print(num, s2)
