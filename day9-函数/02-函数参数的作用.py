"""
需求：
1、计算 x2 的函数
2、计算 xn 的函数
"""


def power(x):
    print(x * x)


power(5)


def power_n(x, n=2):
    res = 1
    i = 1
    while i <= n:
        res *= x
        i += 1
    print(res)


power_n(5, 1)  # 5的1次方
power_n(5, 2)  # 5的2次方
power_n(5, 3)  # 5的3次方
power_n(5, 4)  # 5的4次方
power_n(5)  # 5的2次方
