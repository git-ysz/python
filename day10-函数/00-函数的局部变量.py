"""
变量作用域：变量生效的范围
1、局部变量
2、全局变量
"""
a = 10  # 全局变量


def testA():
    b = 100  # 局部变量
    print(a)
    print(b)


testA()
print(b)  # 报错name 'a' is not defined
