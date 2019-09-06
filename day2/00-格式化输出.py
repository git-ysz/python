"""
1、准备数据
2、格式化符号输出数据
"""
age = 18
name = 'tom'
weight = 65.5
stu_id = 1
stu_id2 = 1000

# 1.今年我的年龄是x岁 -- 整数 -- %d
print('今年我的年龄是%d岁' % age)

# 2.我的名字是xxx -- 字符串 -- %s
print('我的名字是%s' % name)

# 3.我的体重是x公斤 -- 浮点数 -- %f
print('我的体重是%f公斤' % weight)  # 默认保留6位小数
print('我的体重是%.2f公斤' % weight)  # 保留两位小数

# 4.我的学号是x -- 整数 -- %d
print('我的学号是%d' % stu_id)
# 延伸 - 4.1.我的学号是001
print('我的学号是%03d' % stu_id)  # 三位整数不足以0补全
print('我的学号是%03d' % stu_id2)  # 三位整数，超出的按原样输出

# 5.我的名字是xxx，今年x岁了
print('我的名字是%s，年龄%d岁了' % (name, age))
# 延伸 - 5.1.我的名字是xxx，今年x岁了，明年x岁
print('我的名字是%s，今年%d岁了，明年%d岁' % (name, age, age + 1))

# 6.我的名字是xxx，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d' % (name, age, weight, stu_id))
