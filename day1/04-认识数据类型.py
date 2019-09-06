"""
1、按经验将不同的变量存储不同的类型的数据
2、验证这些数据到底是什么数据 -- 检测数据类型 -- type（数据）
"""
# int -- 整形，整数
num1 = 1

# float -- 浮点型，小数
num2 = 1.1
print(type(num1))
print(type(num2))

# str -- 字符串，特点：数据都要带引号
a = 'hello world'
print(type(a))

# bool -- 布尔型，通常判断使用，布尔值只有True 和 False
b = True
print(type(b))

"""
数据类型除了以上数据类型（简单数据类型），还存在四种复杂数据类型
1、list -- 列表
2、tuple -- 元组
3、set -- 集合
4、dict -- 字典
"""
# list -- 列表
c = [10, 20, 30]
print(type(c))

# tuple -- 元组
d = (10, 20, 30)
print(type(d))

# set -- 集合
e = {10, 20, 30}
print(type(e))

# dict -- 字典 -- 键值对
f = {'name': '小明', 'age': 18}
print(type(f))
