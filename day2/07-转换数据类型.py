# 1、float() -- 将数据转换成浮点数型
num = 1
str1 = '10'
print(float(num))  # 1.0
print(type(float(num)))  # float
print(float(str1))  # 10.0

# 2、str() -- 将数据转换成字符串型
print(type(str(num)))

# 3、tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))  # (10, 20, 30)

# 4、list() -- 将一个序列转换成列表
tl = (101, 202, 303)
print(list(tl))  # [101, 202, 303]

# 5、eval() -- 计算字符串中的有效Python表达式，并返回一个对象
# 将字符串内的数据，转换成原有数据类型
str2 = '1'
str3 = '1.1'
str4 = '(10, 20, 30)'
str5 = '[10, 20, 30]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
