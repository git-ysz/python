"""
语法：
try：
    可能发生错误的代码
except 异常类型：
    如果捕获到该异常类型执行的代码

注意：
    1、如果尝试执行的代码的异常类型和要捕获的类型不一致，则无法捕获异常
    2、一般try下发只放一行尝试执行的代码
"""
# 捕获指定异常类型
try:
    # 找不到num变量
    print(num)
except NameError:
    print('NameError：', NameError.__dict__)

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0不能做被除数')


# 捕获多个指定异常
try:
    # print(arr)
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print('捕获多个指定异常')


# 获取异常信息 {ErrorType} as result
try:
    # print(arr)
    print(1 / 0)
except (NameError, ZeroDivisionError) as res:
    print('捕获多个指定异常（有异常信息）：', res)


# 捕获所有异常 --- Exception
try:
    print(arr)
    print(1 / 0)
except Exception as res:
    print('捕获所有异常（有异常信息）：', res)


# 异常之else --- 没有异常时执行的代码
# 异常之finally --- 有无异常都执行的代码
try:
    print(111)
    # print(aaa)
except Exception as res:
    print(res)
else:
    print('else')
finally:
    print('finally')
