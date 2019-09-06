"""
需求：有变量a = 10 和 b = 20 ,交换两个变量的值
"""
import sys
# 方法1
a = 10
b = 20
print(a, b)

c = a
a = b
b = c
print(a, b)

# 方法2 --- 常用
e = 100
f = 200
print(e, f)
e, f = f, e
print(e, f)
