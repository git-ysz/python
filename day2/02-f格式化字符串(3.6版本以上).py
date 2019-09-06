"""
f字符串格式化
版本：Python3.6版本中新增方法
该方法更简单易读，推荐使用
"""
name = 'tom'
age = 18

# 我的名字是xxx，今年x岁了
print('我的名字是%s，今年%s岁了' % (name, age))

# 语法：f'{表达式}'
print(f'我的名字是{name}, 今年{age}岁了')
