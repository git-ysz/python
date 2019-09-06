"""
如果函数有一个返回值，并且只有一句代码，可以使用lambda简化
作用：化简函数代码，占用内存小于函数！！！
语法：lambda 参数列表: 表达式
参数：同函数相同
"""


# 函数
def fn1():
    return 100


print(fn1, fn1())

# lambda 匿名函数
fn2 = lambda: 200

print(fn2, fn2())
