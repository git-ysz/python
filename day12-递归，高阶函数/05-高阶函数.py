"""
把函数作为参数传入，这样的函数称为高阶函数
高阶函数是函数式编程的体现
函数式变成就是指这种高度抽象的编程范式
"""
print(round(1.445, 2))
print(abs(-10))


def sum_num(a, b, fn, *args, **kwargs):
    return fn(a, *args, **kwargs) + fn(b, *args, **kwargs)


print(sum_num(-10, 20, abs))
print(sum_num(10.545, 20.455, round, 1))
