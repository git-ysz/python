import functools

list1 = [1, 2, 3, 4, 5]

# 1.map() -- 对每一项做某件事，返回一个迭代器
res1 = map(lambda x: x**2, list1)
print(list(res1))

# 2. reduce -- 第一个函数参数内有两个参数，累计计算
res2 = functools.reduce(lambda p, n: p + n, list1, 100)
print(res2)

# 3. filter -- 过滤，返回True则保留
res3 = filter(lambda x: not x % 2, list1)  # 过滤掉奇数
print(list(res3))
